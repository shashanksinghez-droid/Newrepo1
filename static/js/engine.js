const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

let width, height;
const resize = () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
};
window.onresize = resize;
resize();

// --- Game Logic Constants ---
const ROAD_WIDTH = 2000;
const SEGMENT_LENGTH = 200;
const RENDER_DISTANCE = 300;
const CAMERA_HEIGHT = 1000;
const CAMERA_DEPTH = 0.8;

// --- State ---
let position = 0;
let speed = 0;
let maxSpeed = 250;
let accel = 1.2;
let playerX = 0;
let playerZ = 1.5 * SEGMENT_LENGTH;
let segments = [];

// Input
const keys = {};
window.onkeydown = e => keys[e.code] = true;
window.onkeyup = e => keys[e.code] = false;

// Generate Road
for (let i = 0; i < 5000; i++) {
    segments.push({
        index: i,
        p1: { world: { z: i * SEGMENT_LENGTH }, screen: { x: 0, y: 0, w: 0 } },
        p2: { world: { z: (i + 1) * SEGMENT_LENGTH }, screen: { x: 0, y: 0, w: 0 } },
        curve: Math.sin(i / 30) * 2, // Procedural curves
        color: (Math.floor(i / 3) % 2) ? { road: '#111', grass: '#000', rumble: '#0ff' } : { road: '#000', grass: '#050505', rumble: '#f0f' }
    });
}

function project(p, cameraX, cameraY, cameraZ) {
    p.camera = {
        x: (p.world.x || 0) - cameraX,
        y: (p.world.y || 0) - cameraY,
        z: (p.world.z || 0) - cameraZ
    };
    const scale = CAMERA_DEPTH / p.camera.z;
    p.screen.x = Math.round((width / 2) + (scale * p.camera.x * width / 2));
    p.screen.y = Math.round((height / 2) - (scale * p.camera.y * height / 2));
    p.screen.w = Math.round(scale * ROAD_WIDTH * width / 2);
}

function drawPolygon(x1, y1, w1, x2, y2, w2, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.moveTo(x1 - w1, y1);
    ctx.lineTo(x2 - w2, y2);
    ctx.lineTo(x2 + w2, y2);
    ctx.lineTo(x1 + w1, y1);
    ctx.closePath();
    ctx.fill();
}

function drawPlayer() {
    const x = width / 2;
    const y = height - 100;
    
    // Draw Bike (Simplified HD Sprite)
    ctx.shadowBlur = 20;
    ctx.shadowColor = '#0ff';
    ctx.fillStyle = '#fff';
    
    // Body
    ctx.fillRect(x - 20, y - 40, 40, 20);
    // Wheels
    ctx.fillStyle = '#0ff';
    ctx.fillRect(x - 25, y - 20, 10, 20);
    ctx.fillRect(x + 15, y - 20, 10, 20);
    // Neon Streak
    ctx.strokeStyle = '#f0f';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x - (playerX * 100), y + 50);
    ctx.stroke();
    ctx.shadowBlur = 0;
}

function update(dt) {
    // Movement Logic
    if (keys['KeyW'] || keys['ArrowUp']) speed += accel;
    else speed *= 0.98;
    
    if (keys['KeyA'] || keys['ArrowLeft']) playerX -= 0.02 * (speed/maxSpeed);
    if (keys['KeyD'] || keys['ArrowRight']) playerX += 0.02 * (speed/maxSpeed);
    
    speed = Math.min(Math.max(speed, 0), maxSpeed);
    position += speed;
    
    // UI Update
    document.getElementById('speed').innerText = Math.round(speed) + " KM/H";
    document.getElementById('distance').innerText = "DIST: " + (position/10000).toFixed(2) + " KM";
}

function render() {
    ctx.clearRect(0, 0, width, height);
    
    // Draw Background (Static Night Sky)
    const grad = ctx.createLinearGradient(0, 0, 0, height);
    grad.addColorStop(0, '#000010');
    grad.addColorStop(0.5, '#100020');
    grad.addColorStop(1, '#000');
    ctx.fillStyle = grad;
    ctx.fillRect(0,0, width, height);

    const baseSegment = segments[Math.floor(position / SEGMENT_LENGTH) % segments.length];
    let dx = -(baseSegment.curve * (position % SEGMENT_LENGTH / SEGMENT_LENGTH));
    let x = 0;

    for (let n = 0; n < RENDER_DISTANCE; n++) {
        const segment = segments[(baseSegment.index + n) % segments.length];
        project(segment.p1, (playerX * ROAD_WIDTH) - x, CAMERA_HEIGHT, position);
        project(segment.p2, (playerX * ROAD_WIDTH) - x - segment.curve, CAMERA_HEIGHT, position);
        
        x += dx;
        dx += segment.curve;

        if (segment.p1.camera.z <= CAMERA_DEPTH) continue;

        const p1 = segment.p1.screen;
        const p2 = segment.p2.screen;

        // Draw Grass/Back
        ctx.fillStyle = segment.color.grass;
        ctx.fillRect(0, p2.y, width, p1.y - p2.y);

        // Draw Road
        drawPolygon(p1.x, p1.y, p1.w, p2.x, p2.y, p2.w, segment.color.road);
        // Draw Rumble Strips (Neon edges)
        drawPolygon(p1.x, p1.y, p1.w * 1.1, p2.x, p2.y, p2.w * 1.1, segment.color.rumble);
    }
    
    drawPlayer();
}

function frame() {
    update();
    render();
    requestAnimationFrame(frame);
}

frame();
