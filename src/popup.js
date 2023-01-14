var yt_video_regex =
  /^https?:\/\/(www\.)?youtube\.com\/watch\?v=[a-zA-Z0-9_-]{11}(&[^#]*)?$/;
if (document.querySelector('input[name="genderS"]:checked').value === 0)
  var api = "";

document.addEventListener("DOMContentLoaded", function () {
  // Get the input element
  var input_url = document.getElementById("yt-url");
  // Set the value of the input to the current URL
  browser.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    // Set the value of the input to the URL of the active tab
    if (yt_video_regex.test(tabs[0].url)) input_url.value = tabs[0].url;
  });

  var summarize_button = document.getElementById("summarize");

  // Attach the click event listener to the button
  summarize_button.addEventListener("click", function () {
    // Get the current URL
    var url = input_url.value;
    var videoId = url.replace(yt_video_regex, "$2");
    // Make an HTTP GET request to the API, passing the URL as a query parameter
    var result = document.getElementById("result");
    fetch(" http://127.0.0.1:8000", {
      method: "GET",
    })
      .then((res) => {
        if (res.ok) {
          return res.json();
        }
        return Promise.reject(res);
      })
      .then((data) => (result.innerHTML = data.summary))
      .catch((res) =>
        res.json().then((e) => {
          result.innerHTML = e.detail;
        })
      );
  });
});
