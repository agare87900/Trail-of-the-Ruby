<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trail of the Ruby 0.0.1 indev</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="game">
        <div id="music-controls">
            <label for="music-volume">🔊 Music:</label>
            <input type="range" id="music-volume" min="0" max="100" value="30">
            <input type="file" id="music-file" accept="audio/*" style="font-size:12px;">
        </div>
        <audio id="background-music" loop></audio>

        <h1>Trail of the Ruby</h1>
        <p id="status">can you find the ruby trail</p>
        <p id="stats">Player Health: 100 | Enemy Health: 50</p>
        <p id="money">Gold Nuggets: 0</p>
        <div id="battlefield">
            <div class="sprite-container">
                <div id="player-sprite" class="sprite player"></div>
                <div class="sprite-label">Player</div>
            </div>
            <div class="sprite-container">
                <div id="enemy-sprite" class="sprite enemy"></div>
                <div class="sprite-label">Enemy</div>
            </div>
        </div>

        <div id="controls">
            <button id="attack">Attack</button>
            <button id="heal">Heal (5 Gold)</button>
            <button id="upgrade">Buy Damage Upgrade (15 Gold)</button>
            <button id="next" disabled>Next Fight</button>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
