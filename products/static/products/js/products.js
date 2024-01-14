// function creates list of immages to be jumped to a specific picture.
function slider() {
  const slides = document.querySelectorAll('.slide');
  const skipsContainer = document.querySelector('.image_skips');
  
  const imageLinks = [];

  let curSlide = 0;
  const maxSlide = slides.length;
  
  // Functions
  
  function createImageLinksArray() {
    const images = document.querySelectorAll('.slide img'); // Get all img tags within elements with class 'slide'

    images.forEach(img => {
        const src = img.getAttribute('src'); 
        imageLinks.push(src); 
    });

  }
  
  function createImageList(imageLinks) {
    let counter = 0

    imageLinks.forEach(link => {
      const listItem = document.createElement('li');
      const image = document.createElement('img'); 
      image.src = link;
      image.alt = `Slide ${counter}`;
      listItem.classList.add('image_skips_picture');
      listItem.dataset.slide = counter;
      counter++;

      listItem.appendChild(image);
      skipsContainer.appendChild(listItem);
    });
  }

  function activateSlide(slide) {
    document
      .querySelectorAll('.image_skips_picture')
      .forEach(slide => slide.classList.remove('image_skips_picture--active'));

    document
      .querySelector(`.image_skips_picture[data-slide="${slide}"]`)
      .classList.add('image_skips_picture--active');
  };

  function goToSlide(slide){
    slides.forEach(
      (s, i) => (s.style.transform = `translateX(${100 * (i - slide)}%)`)
    );
  };
  
  function nextSlide() {
    if (curSlide === maxSlide - 1) {
      curSlide = 0;
    } else {
      curSlide++;
    }
    goToSlide(curSlide);
    activateSlide(curSlide);
  };

  function prevSlide() {
    if (curSlide === 0) {
      curSlide = maxSlide - 1;
    } else {
      curSlide--;
    }
    goToSlide(curSlide);
    activateSlide(curSlide);
  };

  function init() {
    createImageLinksArray()
    createImageList(imageLinks)
    goToSlide(0);
    activateSlide(0);
  };
  init();

  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft') prevSlide();
    e.key === 'ArrowRight' && nextSlide();
  });

  skipsContainer.addEventListener('click', function (e) {
    if (e.target.classList.contains('image_skips_picture')) {
      const { slide } = e.target.dataset;
      goToSlide(slide);
      activateSlide(slide);
    }
    else if (e.target.parentNode.classList.contains('image_skips_picture')) {
     const { slide } = e.target.parentNode.dataset;
      goToSlide(slide);
      activateSlide(slide);
    }
  });
};
slider();

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl, {
            customClass: 'custom-tooltip'
        }))