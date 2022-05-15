 const setBg = (column, heading) => {
    const randomColor = Math.floor(Math.random()*16777215).toString(16);
    const colOne = document.getElementById(column);
    colOne.style.backgroundColor = "#" + randomColor;
    const headOne = document.getElementById(heading);
    headOne.innerHTML = "#" + randomColor;
}

function copyDivToClipboard(heading) {
    const range = document.createRange();
    range.selectNode(document.getElementById(heading));
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand("copy");
    window.getSelection().removeAllRanges();
    alert("Copied to clipboard!");
}
