var slideIndex = 1;
document.getElementById("photo").style.display = "none"
showSlides(slideIndex);

function upload(e){
  pathname = document.getElementById("photo").value;
  document.getElementById("inputIMG").innerHTML = pathname.split('\\').pop().split('/').pop();
}

document.getElementById("photo").addEventListener('input',upload,false);



const _C = document.querySelector('.slideshow-container');

function unify(e) { return e.changedTouches ? e.changedTouches[0] : e };

let x0 = null,
    y0 = null;

function lock(e) { 
  x0 = unify(e).clientX;
  y0 = unify(e).clientY; 

};

let i = 0;

function move(e) {
  if(x0 || x0 === 0) {
    let dx = unify(e).clientX - x0, sx = Math.sign(dx);
    let dy = unify(e).clientY - y0, sy = Math.sign(dx);
    if (sx!=0 && Math.abs(dx) > Math.abs(dy)){
      plusSlides(sx);
    }
    x0 = null;
    y0 = null;
  }
};

_C.addEventListener('mousedown', lock, false);
_C.addEventListener('touchstart', lock, false);

_C.addEventListener('mouseup', move, false);
_C.addEventListener('touchend', move, false);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var captions = document.getElementsByClassName("myCaptions");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1} 
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none"; 
      captions[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  captions[slideIndex-1].style.display = "block";
  document.getElementById("model").value= captions[slideIndex-1].id; 
  dots[slideIndex-1].className += " active";
}