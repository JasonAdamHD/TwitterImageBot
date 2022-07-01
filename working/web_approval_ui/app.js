const baseURL = 'http://192.168.1.229:5000/'
let filename = ""

window.onload = function(){
     loadImage(baseURL);
     document.getElementById('approve').addEventListener("click", approved);
     document.getElementById('deny').addEventListener("click", denied);
     document.getElementById('skip').addEventListener("click", loadImage);
}

function makeResp(url){

}

async function approved(){
     const approvedURL = baseURL + 'approved'
     const response = await fetch(approvedURL, {
          method: "PUT",
          headers: {
               'content-type': 'application/json'
          },
          body: JSON.stringify(
               {
                    "filename" : filename
               }
          )
     })
     loadImage()
}

async function denied(){
     const deniedURL = baseURL + 'denied'
     const response = await fetch(deniedURL, {
          method: "PUT",
          headers: {
               'content-type': 'application/json'
          },
          body: JSON.stringify(
               {
                    "filename" : filename
               }
          )
     })
     loadImage()
}

/****************************************
  Get image from server and display it
****************************************/
async function loadImage() {
     fetchImage();
}

async function fetchImage() {
     const randomImageURL = baseURL + 'random_image'
     const response = await fetch(randomImageURL);
     const blob = await response.blob();

     const url = URL.createObjectURL(blob);

     const image = new Image();
     image.src = url;

     document.getElementById('pic').src = image.src
     filename = response.headers.get("Content-Disposition").split("filename=")[1]
}