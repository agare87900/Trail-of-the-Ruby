let player = { health: 100, attackPower: 20, money: 0 };
let enemy = { health: 50, attackPower: 10 };
let fightCount = 0;

const statusEl = document.getElementById('status');
const statsEl = document.getElementById('stats');
const moneyEl = document.getElementById('money');
const attackBtn = document.getElementById('attack');
const healBtn = document.getElementById('heal');
const upgradeBtn = document.getElementById('upgrade');
const nextBtn = document.getElementById('next');
const enemySprite = document.getElementById('enemy-sprite');
const playerSprite = document.getElementById('player-sprite');

function updateStatus() {
    statsEl.textContent = `Player Health: ${player.health} | Enemy Health: ${enemy.health}`;
    moneyEl.textContent = `Gold Nuggets: ${player.money}`;
}

function attack() {
    // Visual player attack then apply damage and handle counterattack
    disableControls();
    playerSprite.classList.add('attack-anim');
    setTimeout(() => {
        playerSprite.classList.remove('attack-anim');
        // apply damage to enemy
        enemy.health -= player.attackPower;
        enemySprite.classList.add('hit-flash');
        setTimeout(() => enemySprite.classList.remove('hit-flash'), 440);
        updateStatus();

        if (enemy.health <= 0) {
            handleVictory();
            return;
        }

        // enemy counterattack animation
        setTimeout(() => {
            enemySprite.classList.add('enemy-attack-anim');
            setTimeout(() => {
                enemySprite.classList.remove('enemy-attack-anim');
                player.health -= enemy.attackPower;
                playerSprite.classList.add('hit-flash');
                setTimeout(() => playerSprite.classList.remove('hit-flash'), 440);
                updateStatus();
                if (player.health <= 0) {
                    handleGameOver();
                    return;
                }
                enableControls();
            }, 320);
        }, 180);
    }, 320);
}

function heal() {
    if (player.money >= 5) {
        disableControls();
        player.money -= 5;
        player.health += 20;
        statusEl.textContent = 'You healed for 20 health!';
        // small heal visual
        playerSprite.classList.add('shake');
        setTimeout(() => playerSprite.classList.remove('shake'), 240);
        updateStatus();

        // enemy gets a free counterattack if still alive
        if (enemy.health > 0) {
            setTimeout(() => {
                enemySprite.classList.add('enemy-attack-anim');
                setTimeout(() => {
                    enemySprite.classList.remove('enemy-attack-anim');
                    player.health -= enemy.attackPower;
                    playerSprite.classList.add('hit-flash');
                    setTimeout(() => playerSprite.classList.remove('hit-flash'), 440);
                    if (player.health <= 0) {
                        handleGameOver();
                        return;
                    }
                    updateStatus();
                    enableControls();
                }, 320);
            }, 260);
        } else {
            enableControls();
        }
    } else {
        statusEl.textContent = 'Not enough gold nuggets to heal!';
    }
}

function upgrade() {
    if (player.money >= 15) {
        disableControls();
        player.money -= 15;
        player.attackPower += 5;
        statusEl.textContent = 'Damage upgraded!';
        // upgrade visual: brief glow
        playerSprite.classList.add('hit-flash');
        setTimeout(() => playerSprite.classList.remove('hit-flash'), 440);
        updateStatus();
        setTimeout(() => enableControls(), 360);
    } else {
        statusEl.textContent = 'Not enough gold nuggets!';
    }
}

function nextFight() {
    fightCount++;
    if (fightCount > 20) {
        statusEl.textContent = 'Congratulations! You found the ruby trail!';
        attackBtn.disabled = true;
        healBtn.disabled = true;
        upgradeBtn.disabled = true;
        nextBtn.disabled = true;
        return;
    }
    enemy.health = 50;
    statusEl.textContent = `A new enemy appears! Fight ${fightCount}/20`;
    attackBtn.disabled = false;
    healBtn.disabled = false;
    upgradeBtn.disabled = false;
    nextBtn.disabled = true;
    updateStatus();
}

function disableControls(){
    attackBtn.disabled = true;
    healBtn.disabled = true;
    upgradeBtn.disabled = true;
    nextBtn.disabled = true;
}

function enableControls(){
    attackBtn.disabled = false;
    healBtn.disabled = false;
    upgradeBtn.disabled = false;
    nextBtn.disabled = true;
}

function handleVictory(){
    player.money += 15;
    statusEl.textContent = 'Victory! Click "Next Fight" to continue.';
    attackBtn.disabled = true;
    healBtn.disabled = true;
    upgradeBtn.disabled = true;
    nextBtn.disabled = false;
    updateStatus();
}

function handleGameOver(){
    statusEl.textContent = 'Game Over!';
    attackBtn.disabled = true;
    healBtn.disabled = true;
    upgradeBtn.disabled = true;
    nextBtn.disabled = true;
    updateStatus();
}

attackBtn.addEventListener('click', attack);
healBtn.addEventListener('click', heal);
upgradeBtn.addEventListener('click', upgrade);
nextBtn.addEventListener('click', nextFight);

// Music controls
const backgroundMusic = document.getElementById('background-music');
const musicVolume = document.getElementById('music-volume');
const musicFile = document.getElementById('music-file');

musicVolume.addEventListener('input', (e) => {
    backgroundMusic.volume = e.target.value / 100;
});

musicFile.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        const url = URL.createObjectURL(file);
        backgroundMusic.src = url;
        backgroundMusic.play();
    }
});

// Set initial volume
backgroundMusic.volume = musicVolume.value / 100;

updateStatus();
