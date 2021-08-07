function toContent1(){
    let button =$('.to-content');

    button.on('click', (i)=>{
        i.preventDefault();
        $('html').animate({scrollTop: 920}, 1000);
    })
}

toContent1();
