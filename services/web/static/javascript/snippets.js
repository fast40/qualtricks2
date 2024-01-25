const javascriptCodeElement = document.getElementById("javascript");
const htmlCodeElement = document.getElementById("html");

const datasetNameSelector = document.querySelector("select[name=dataset_id]");
const orderingSelector = document.querySelector("select[name=ordering]");

function generateSnippets() {
    javascriptCodeElement.textContent = generateJavascript(datasetNameSelector.value);
    htmlCodeElement.textContent = generateHTML(datasetNameSelector.value);

    javascriptCodeElement.parentElement.style.display = "initial";
}

function generateJavascript(dataset_id) {
    return `const embeddedDataField = "Video" + String("\${lm://CurrentLoopNumber}");
const xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        Qualtrics.SurveyEngine.setEmbeddedData(embeddedDataField, xhttp.responseText);
    }
};
xhttp.open("GET", "http://localhost/get_file?dataset_id=${dataset_id}&response_id=\${e://Field/ResponseID}&loop_number=\${lm://CurrentLoopNumber}&redirect=false", true);
xhttp.send();`;
}

function generateHTML(dataset_id) {
    return `<video class="inserted-video" style="width: 100%;" controls playsinline controlsList="noplaybackrate">
<source id="video-source" src="http://localhost/get_file?dataset_id=${dataset_id}&response_id=\${e://Field/ResponseID}&loop_number=\${lm://CurrentLoopNumber}&redirect=true" type="video/mp4">
Your browser does not support the video tag.
</video>`;
}
