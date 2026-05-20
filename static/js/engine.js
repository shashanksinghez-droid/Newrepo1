const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let w, h;
const setSize = () => {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
};
window.onresize = setSize;
setSize();

let score = 0;
let speed = 0.05;
let playerX = 0;
let targetPlayerX = 0;
const blocks = [];

// Input Handling
const keys = {};
window.onkeydown = (e) => keys[e.code] = true;
window.onkeyup = (e) => keys[e.code] = false;

class CyberBlock {
    constructor(z) {
        this.init(z);
    }

    init(z) {
        this.z = z;
        this.x = (Math.random() - 0.5) * 8;
        this.y = (Math.random() - 0.5) * 8;
        this.size = 0.8 + Math.random() * 2;
        this.color = `hsl(${180 + Math.random() * 60}, 100%, 50%)`;
        this.hue = 180 + Math.random() * 60;
    }

    update() {
        this.z -= speed;
        
        // Smooth movement logic
        if (keys['ArrowLeft'] || keys['KeyA']) targetPlayerX += 0.005;
        if (keys['ArrowRight'] || keys['KeyD']) targetPlayerX -= 0.005;
        playerX += (targetPlayerX - playerX) * 0.1;

        if (this.z <= 0) {
            this.init(15);
            score += 150;
        }
    }

    draw() {
        const perspective = 600 / this.z;
        const xPos = w/2 + (this.x + playerX) * perspective;
        const yPos = h/2 + this.y * perspective;
        const s = this.size * perspective;

        // Bloom Effect
        ctx.shadowBlur = 20;
        ctx.shadowColor = this.color;
        ctx.strokeStyle = this.color;
        ctx.lineWidth = 2;
        
        ctx.strokeRect(xPos - s/2, yPos - s/2, s, s);
        
        // Inner Glow
        ctx.globalAlpha = 0.1;
        ctx.fillStyle = this.color;
        ctx.fillRect(xPos - s/2, yPos - s/2, s, s);
        ctx.globalAlpha = 1.0;
    }
}

// Generate Tunnel
for(let i = 0; i < 50; i++) blocks.push(new CyberBlock(i * 0.3));

function animate() {
    // Persistent Trails
    ctx.fillStyle = 'rgba(0, 5, 10, 0.2)';
    ctx.fillRect(0, 0, w, h);

    // Draw Cyber-Grid
    ctx.strokeStyle = 'rgba(0, 255, 255, 0.05)';
    ctx.lineWidth = 1;
    for(let i=0; i < w; i += 100) {
        ctx.beginPath(); ctx.moveTo(i, 0); ctx.lineTo(i, h); ctx.stroke();
    }

    // Sort by depth for 3D realism
    blocks.sort((a, b) => b.z - a.z);
    
    blocks.forEach(b => {
        b.update();
        b.draw();
    });

    document.getElementById('score').innerText = `UPTIME: ${String(score).padStart(6, '0')}`;
    speed += 0.00002;
    requestAnimationFrame(animate);
}

animate();
