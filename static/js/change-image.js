var image = document.querySelector('#img');
var imageView = document.querySelector('.image-form img');
var iamgeBtn = document.querySelector('.image-form button');


iamgeBtn.addEventListener('click',()=>{
    image.click()
})


image.addEventListener('change',(e)=>{
    var image_url = URL.createObjectURL(e.target.files[0])
    imageView.src = image_url;
})