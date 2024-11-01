
function downloadFile() {
    const aTag = document.createElement("a")
    aTag.href = "./test.txt"
    aTag.download = "FreeMoney.txt"
    aTag.click()
}

window.onload(downloadFile())
