import { ytsapi } from "./env/ytsapi.js";

const yt_video_regex =
  /^https?:\/\/(www\.)?youtube\.com\/watch\?v=[a-zA-Z0-9_-]{11}(&[^#]*)?$/;
let api = ytsapi + "/api/summarizer-abstractive/transcript";


document.addEventListener("DOMContentLoaded", function () {
  // Get the input element
  var input_url = document.getElementById("yt-url");
  var result = document.getElementById("result");
  var spinner = document.getElementById("spinner");
  // Set the value of the input to the current URL
  browser.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    // Set the value of the input to the URL of the active tab
    if (yt_video_regex.test(tabs[0].url)) input_url.value = tabs[0].url;
  });

  var summarize_button = document.getElementById("summarize");

  // Attach the click event listener to the button
  summarize_button.addEventListener("click", function () {
    if (yt_video_regex.test(input_url.value)) {
      if (document.querySelector('input[name="summary-type"]:checked').value === "1")
  api = ytsapi + "/api/summarizer-extractive/transcript";
      // Get the current URL
      var url = new URL(input_url.value);
      var videoId = url.searchParams.get("v");
      spinner.style.display = "block";
      result.innerHTML = "";
      fetch(api + `/${videoId}/`, {
        method: "GET",
      })
        .then((res) => {
          if (res.ok) {
            return res.json();
          }
          return Promise.reject(res);
        })
        .then((data) => {
          spinner.style.display = "none";
          result.style.color = "black";
          result.innerHTML = data.summary;
        })
        .catch((res) =>
          res.json().then((e) => {
            spinner.style.display = "none";
            result.style.color = "red";
            result.innerHTML = e.detail;
          })
        );
    } else {
      result.style.color = "red";
      result.innerHTML = "Invalid URL";
    }
  });
});
