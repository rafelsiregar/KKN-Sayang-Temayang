

$(document).ready(function(){
    $('#login').click(function(){
        window.location.href = '/admin';
    })
    news_card = document.getElementsByClassName('card-text')
    
    for(var i=0;i<news_card.length;i++){
        console.log(news_card[i].innerHTML);
        news_card[i].innerHTML = truncate(news_card[i].innerHTML, 100, '...')
    }
    
})

const truncate = (str, max, suffix) => 
str.length < max ? str : `${str.substring(0, str.substring(0, max - suffix.length).lastIndexOf(' '))}${suffix}`;


