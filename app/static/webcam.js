const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
canvas.style.display = "none";
const width = 256;
const height = 256;
canvas.width = width;
canvas.height = height;
const similarity_paragraph = document.getElementById('similarity');
const access_paragraph = document.getElementById('access');
const text_paragraph = document.getElementById('text');
const webcam_timeout = 1000; //ms


navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;

startVideo();
function startVideo() {
  navigator.getUserMedia(
  {
    video: {}
  },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}

video.addEventListener('play', () => {
  setInterval(async () => {
    var context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, width, height);
    var image = canvas.toDataURL('image/png');

    let data = {image: image};

    (async () => {
      const rawResponse = await fetch('/check', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      const content = await rawResponse.json();

      similarity_paragraph.textContent = "similarity: " + content.similarity.toFixed(2).toString() + "%"
      access_paragraph.textContent = "access: " + content.access
      text_paragraph.textContent = content.text
    })();

  }, webcam_timeout)
})
