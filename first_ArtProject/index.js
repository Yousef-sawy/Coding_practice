let container = document.querySelector(".container");
let gridButton = document.getElementById("submit-grid");
let clearGridButton = document.getElementById("clear-grid");
let gridWidth = document.getElementById("width-range");
let gridHeight = document.getElementById("height-range");
let colorButton = document.getElementById("color-input");
let eraseBtn = document.getElementById("erase-btn");
let paintBtn = document.getElementById("paint-btn");
let widthValue = document.getElementById("width-value");
let heightValue = document.getElementById("height-value");

let events = {
    mouse: {
        down: "mousedown",
        move: "mousemove",
        up: "mouseup"
    },
    touch: {
        down: "touchstart",
        move: "touchmove",
        up: "touchend",
    },
};

let deviceType = "mouse"; // Default to mouse
let draw = false;
let erase = false;

// Improved touch detection
const isTouchDevice = () => 'ontouchstart' in window || navigator.maxTouchPoints > 0;
deviceType = isTouchDevice() ? "touch" : "mouse";

isTouchDevice();

gridButton.addEventListener("click", () => {
    container.innerHTML = "";
    const height = gridHeight.value;
    const width = gridWidth.value;
    let count = 0;

    for (let i = 0; i < height; i++) {
        count += 2;
        let div = document.createElement("div");
        div.classList.add("gridRow");

        for (let j = 0; j < width; j++) {
            count += 2;
            let col = document.createElement("div");
            col.classList.add("gridCol");
            col.setAttribute("id", `gridCol${count}`);

            // Event listeners for drawing/erasing
            col.addEventListener(events[deviceType].down, () => {
                draw = true;
                col.style.backgroundColor = erase ? "transparent" : colorButton.value;
            });

            col.addEventListener(events[deviceType].move, (e) => {
                const x = !isTouchDevice() ? e.clientX : e.touches[0].clientX;
                const y = !isTouchDevice() ? e.clientY : e.touches[0].clientY;
                const elementId = document.elementFromPoint(x, y).id;
                checker(elementId);
            });

            col.addEventListener(events[deviceType].up, () => {
                draw = false;
            });

            div.appendChild(col);
        }

        container.appendChild(div);
    }
});

function checker(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        if (draw) {
            element.style.backgroundColor = erase ? "transparent" : colorButton.value;
        }
    }
}

clearGridButton.addEventListener("click", () => {
    container.innerHTML = "";
});

eraseBtn.addEventListener("click", () => {
    erase = true;
});

paintBtn.addEventListener("click", () => {
    erase = false;
});

gridWidth.addEventListener("input", () => {
    widthValue.innerHTML = gridWidth.value < 9 ? `0${gridWidth.value}` : gridWidth.value;
});

gridHeight.addEventListener("input", () => {
    heightValue.innerHTML = gridHeight.value < 9 ? `0${gridHeight.value}` : gridHeight.value;
});

window.onload = () => {
    gridHeight.value = 0;
    gridWidth.value = 0;
};