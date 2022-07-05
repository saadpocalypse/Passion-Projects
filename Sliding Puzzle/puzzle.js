const rows = 3;
const columns = 3;
let currTile;
let moveCount = 0;
const imgOrder = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
const folders = ["Moon Knight/", "Homelander/", "Daredevil/", "Joker/", "Soldier Boy/", "US Agent/", "Deadpool/"];
const directions = ["Up", "Down", "Left", "Right"];
const folderPicked = pickFolder(folders);
const movesToSolve = [];
let winningCondition = false;
let timer;

window.onload = function(){
    timer = (document.getElementById("stopwatch"));
    let shuffledArray = trueShuffle(imgOrder);
    for (let counter = 0; counter < rows; counter++){
        for (let counterTwo = 0; counterTwo < columns; counterTwo++){
            let tile = document.createElement("img");
            tile.id = counter.toString() + "-" + counterTwo.toString();
            tile.src = folderPicked + shuffledArray.shift() + ".jpg";
            tile.addEventListener("mousedown", clickSwitch);
            tile.addEventListener("mouseup", clickOver);
            document.getElementById("puzzleBoard").append(tile);

        }
    }
}

function clickSwitch(){
    currTile = this;
}

async function clickOver(){
    if (winningCondition === false) {
        let otherTile;
        const boxes = [];
        const boxesAgain = [];

        let currCoords = currTile.id.split("-");
        let r = parseInt(currCoords[0]);
        let c = parseInt(currCoords[1]);

        const one = document.getElementById("0-0");
        boxes.push(one);
        const two = document.getElementById("0-1");
        boxes.push(two);
        const three = document.getElementById("0-2");
        boxes.push(three);
        const four = document.getElementById("1-0");
        boxes.push(four);
        const five = document.getElementById("1-1");
        boxes.push(five);
        const six = document.getElementById("1-2");
        boxes.push(six);
        const seven = document.getElementById("2-0");
        boxes.push(seven);
        const eight = document.getElementById("2-1");
        boxes.push(eight);
        const nine = document.getElementById("2-2");
        boxes.push(nine);

        for (let counter = 0; counter < 9; counter++) {
            const currentImage = boxes[counter];
            if (currentImage.src.includes("3.jpg")) {
                otherTile = currentImage;
            }
        }

        let otherCoords = otherTile.id.split("-");
        let r2 = parseInt(otherCoords[0]);
        let c2 = parseInt(otherCoords[1]);

        let moveLeft = r === r2 && c2 === c - 1;
        let moveRight = r === r2 && c2 === c + 1;
        let moveUp = c === c2 && r2 === r - 1;
        let moveDown = c === c2 && r2 === r + 1;

        if (moveLeft) {
            addToList("right", "left");
        }
        if (moveRight) {
            addToList("left", "right");
        }
        if (moveUp) {
            addToList("down", "up");
        }
        if (moveDown) {
            addToList("up", "down");
        }

        let isAdjacent = moveLeft || moveRight || moveUp || moveDown;

        if (isAdjacent) {
            let currImg = currTile.src;
            currTile.src = otherTile.src;
            otherTile.src = currImg;

            moveCount += 1;
            if (moveCount === 1){
                startTimer();
            }
            document.getElementById("moveCount").innerText = moveCount;
        }

        const one_again = document.getElementById("0-0");
        boxesAgain.push(one_again);
        const two_again = document.getElementById("0-1");
        boxesAgain.push(two_again);
        const three_again = document.getElementById("0-2");
        boxesAgain.push(three_again);
        const four_again = document.getElementById("1-0");
        boxesAgain.push(four_again);
        const five_again = document.getElementById("1-1");
        boxesAgain.push(five_again);
        const six_again = document.getElementById("1-2");
        boxesAgain.push(six_again);
        const seven_again = document.getElementById("2-0");
        boxesAgain.push(seven_again);
        const eight_again = document.getElementById("2-1");
        boxesAgain.push(eight_again);
        const nine_again = document.getElementById("2-2");
        boxesAgain.push(nine_again);

        await winChecker(boxesAgain);
    }
}

async function winChecker(array){
    if(array[0].src.includes("1.jpg") && array[1].src.includes("2.jpg") && array[2].src.includes("3.jpg")
        && array[3].src.includes("4.jpg") && array[4].src.includes("5.jpg") && array[5].src.includes("6.jpg") &&
        array[6].src.includes("7.jpg") && array[7].src.includes("8.jpg") && array[8].src.includes("9.jpg")){
        if(document.getElementById("btn").innerText.includes("Hide")){
            tileNumbers();
        }
        await sleep(20);
        let button = document.getElementById("solve");
        button.disabled = true;
        button.style.backgroundColor = "#C2C2C2FF";
        button.style.cursor = "default";
        alert("Congratulations, you win!");
        winningCondition = true;
        stopTimer();
    }
}

function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
}

function pickFolder(arr){
    const randomIndex = Math.floor(Math.random() * arr.length);
    return arr[randomIndex];
}


/* Not every slide-puzzle orientation is solvable. Initially, I was just randomly shuffling the array
and presenting it to the user to solve but some of them were unsolvable. The function below shuffles the
array in such a way that it can still be solved.
 */

function trueShuffle(arr) {
    let arrTwoD = [[], [], []];
    for (let i = 0; i < 9; i++) {
        if (i < 3) {
            arrTwoD[0].push(arr[i]);
        }
        if (i < 6 && i > 2) {
            arrTwoD[1].push(arr[i]);
        }
        if (i > 5) {
            arrTwoD[2].push(arr[i]);
        }
    }
    let coordinates = [0, 2];
    let turns = 0;

    while (turns < 200){
        let randomIndex = Math.floor(Math.random() * directions.length);
        let move = directions[randomIndex];

        if (move === "Down") {
            if (coordinates[0] !== 2) {
                let blankTile = arrTwoD[coordinates[0]][coordinates[1]];
                arrTwoD[coordinates[0]][coordinates[1]] = arrTwoD[coordinates[0] + 1][coordinates[1]];
                arrTwoD[coordinates[0] + 1][coordinates[1]] = blankTile;
                coordinates = [coordinates[0] + 1, coordinates[1]];
                addToList("down", "up");
                turns++;
            }
        }
        if (move === "Up") {
            if (coordinates[0] !== 0) {
                let blankTile = arrTwoD[coordinates[0]][coordinates[1]];
                arrTwoD[coordinates[0]][coordinates[1]] = arrTwoD[coordinates[0] - 1][coordinates[1]];
                arrTwoD[coordinates[0] - 1][coordinates[1]] = blankTile;
                coordinates = [coordinates[0] - 1, coordinates[1]];
                addToList("up", "down");
                turns++;
            }
        }

        if (move === "Left") {
            if (coordinates[1] !== 0) {
                let blankTile = arrTwoD[coordinates[0]][coordinates[1]];
                arrTwoD[coordinates[0]][coordinates[1]] = arrTwoD[coordinates[0]][coordinates[1] - 1];
                arrTwoD[coordinates[0]][coordinates[1] - 1] = blankTile;
                coordinates = [coordinates[0], coordinates[1] - 1];
                addToList("left", "right");
                turns++;
            }
        }
        if (move === "Right") {
            if (coordinates[1] !== 2) {
                let blankTile = arrTwoD[coordinates[0]][coordinates[1]];
                arrTwoD[coordinates[0]][coordinates[1]] = arrTwoD[coordinates[0]][coordinates[1] + 1];
                arrTwoD[coordinates[0]][coordinates[1] + 1] = blankTile;
                coordinates = [coordinates[0], coordinates[1] + 1];
                addToList("right", "left");
                turns++;
            }
        }
    }

    let arrayToReturn = [];
    for(let row = 0; row < 3; row++){
        for(let column = 0; column < 3; column++){
            arrayToReturn.push(arrTwoD[row][column]);
        }
    }
    return arrayToReturn;
}

function tileNumbers(){
    let boxes = [];
    const one = document.getElementById("0-0");
    boxes.push(one);
    const two = document.getElementById("0-1");
    boxes.push(two);
    const three = document.getElementById("0-2");
    boxes.push(three);
    const four = document.getElementById("1-0");
    boxes.push(four);
    const five = document.getElementById("1-1");
    boxes.push(five);
    const six = document.getElementById("1-2");
    boxes.push(six);
    const seven = document.getElementById("2-0");
    boxes.push(seven);
    const eight = document.getElementById("2-1");
    boxes.push(eight);
    const nine = document.getElementById("2-2");
    boxes.push(nine);
    let state = document.getElementById("btn");
    if (state.innerText.includes("Show")){
        state.innerHTML = "Hide Tile Numbers";
        for (let i = 0; i < 9; i++){
            let element = boxes[i];
            if (element.src.includes("1.jpg")){
                element.src = "Numbers/1.jpg";
            }
            if (element.src.includes("2.jpg")){
                element.src = "Numbers/2.jpg";
            }
            if (element.src.includes("3.jpg")){
                element.src = "Numbers/3.jpg";
            }
            if (element.src.includes("4.jpg")){
                element.src = "Numbers/4.jpg";
            }
            if (element.src.includes("5.jpg")){
                element.src = "Numbers/5.jpg";
            }
            if (element.src.includes("6.jpg")){
                element.src = "Numbers/6.jpg";
            }
            if (element.src.includes("7.jpg")){
                element.src = "Numbers/7.jpg";
            }
            if (element.src.includes("8.jpg")){
                element.src = "Numbers/8.jpg";
            }
            if (element.src.includes("9.jpg")){
                element.src = "Numbers/9.jpg";
            }
        }
    }
    else{
        state.innerHTML = "Show Tile Numbers";
        for (let i = 0; i < 9; i++){
            let element = boxes[i];
            if (element.src.includes("1.jpg")){
                element.src = folderPicked + "1.jpg";
            }
            if (element.src.includes("2.jpg")){
                element.src = folderPicked + "2.jpg";
            }
            if (element.src.includes("3.jpg")){
                element.src = folderPicked + "3.jpg";
            }
            if (element.src.includes("4.jpg")){
                element.src = folderPicked + "4.jpg";
            }
            if (element.src.includes("5.jpg")){
                element.src = folderPicked + "5.jpg";
            }
            if (element.src.includes("6.jpg")){
                element.src = folderPicked + "6.jpg";
            }
            if (element.src.includes("7.jpg")){
                element.src = folderPicked + "7.jpg";
            }
            if (element.src.includes("8.jpg")){
                element.src = folderPicked + "8.jpg";
            }
            if (element.src.includes("9.jpg")){
                element.src = folderPicked + "9.jpg";
            }
        }
    }
}

// document.addEventListener('keyup', (e) =>{
//     if (e.key === 'ArrowUp'){
//         move("up");
//     }
//     else if (e.key === 'ArrowDown'){
//         move("down");
//     }
//     else if (e.key === 'ArrowLeft'){
//         move("left");
//     }
//     else if (e.key === 'ArrowRight'){
//         move("right");
//     }
// });

function findEmptyCell(){
    let coordinates = [];
    let coordinateString = "";
    for(let indexOne = 0; indexOne < 3; indexOne++){
        for(let indexTwo = 0; indexTwo < 3; indexTwo++){
            coordinateString = indexOne + "-" + indexTwo;
            if (document.getElementById(coordinateString).src.includes("3.jpg")){
                coordinates.push(indexOne);
                coordinates.push(indexTwo);
                break;
            }
        }
    }
    return coordinates;
}

function restart(){
    location.reload();
}

function move(arg){
    let positionOfThree = findEmptyCell();
    if (arg === "up"){
        if(positionOfThree[0] !== 2){
            currTile = document.getElementById((positionOfThree[0] + 1) + "-" + (positionOfThree[1]));
            clickOver().then(() => addToList("down", "up"));
        }
    }
    if (arg === "down"){
        if(positionOfThree[0] !== 0){
            currTile = document.getElementById((positionOfThree[0] - 1) + "-" + (positionOfThree[1]));
            clickOver().then(() => addToList("up", "down"));
        }
    }
    if (arg === "left"){
        if(positionOfThree[1] !== 2){
            currTile = document.getElementById((positionOfThree[0]) + "-" + (positionOfThree[1] + 1));
            clickOver().then(() => addToList("right", "left"));
        }
    }
    if (arg === "right"){
        if(positionOfThree[1] !== 0){
            currTile = document.getElementById((positionOfThree[0]) + "-" + (positionOfThree[1] - 1));
            clickOver().then(() => addToList("left", "right"));
        }
    }
}

async function solver(){
    let arrToParse = [];
    for (let counter = movesToSolve.length - 1; counter > -1; counter--){
        arrToParse.push(movesToSolve[counter]);
    }
    for (let moveCount = 0; moveCount < arrToParse.length; moveCount++){
         let moveToMake = arrToParse[moveCount];
         move(moveToMake);
         await sleep(50);
    }
}

function addToList(solve, actual){
    if (movesToSolve.length > 0){
        if(movesToSolve[movesToSolve.length - 1] !== actual){
            movesToSolve.push(solve);
        }
        else{
            movesToSolve.pop();
        }
    }
    else{
        movesToSolve.push(solve);
    }
}



let hr = 0;
let min = 0;
let sec = 0;
let stoptime = true;

function startTimer() {
  if (stoptime === true) {
        stoptime = false;
        timerCycle();
    }
}
function stopTimer() {
  if (stoptime === false) {
    stoptime = true;
  }
}

function timerCycle() {
    console.log("here");
    if (stoptime === false) {
    sec = parseInt(sec);
    min = parseInt(min);
    hr = parseInt(hr);

    sec = sec + 1;

    if (sec === 60) {
      min = min + 1;
      sec = 0;
    }
    if (min === 60) {
      hr = hr + 1;
      min = 0;
      sec = 0;
    }

    if (sec < 10 || sec === 0) {
      sec = '0' + sec;
    }
    if (min < 10 || min === 0) {
      min = '0' + min;
    }
    if (hr < 10 || hr === 0) {
      hr = '0' + hr;
    }

    timer.innerHTML = hr + ':' + min + ':' + sec;
    setTimeout("timerCycle()", 1000);

  }
}
