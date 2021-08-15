

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

function redirect(year, month, slug){
    window.location.href = window.location.origin+"/"+year+"/"+month+"/"+slug;
}



function renderFooter(){
    return `<footer class="footer-32892 py-5">
    <div class="site-section">
      <div class="container">
        <div class="row">
          <div class="col-md pr-md-5 mb-4 mb-md-0">
            <h3>Desa Jono</h3>
            <p class="mb-4">Desa Jono RT 07 RW 02 Kec. Temayang Kab. Bojonegoro
              Kecamatan Temayang Kabupaten Bojonegoro Provinsi Jawa Timur Kode Pos 62184</p>
            <ul class="list-unstyled quick-info mb-4">
              <li class='d-flex flex-icon'>
                <span class="bi bi-telephone"></span>
                <a href="#" class="d-flex align-items-center">+62 353 88XXX</a>
              </li>
              <li class="d-flex flex-icon">
                <span class="bi bi-envelope"></span> 
                <a href="#" class="d-flex align-items-center">desajono00@gmail.com</a>
              </li>
            </ul>

            <form action="#" class="subscribe">
              <input type="text" class="form-control" placeholder="Enter your e-mail">
              <input type="submit" class="btn btn-submit" value="Send">
            </form>
          </div>


          <div class="col-md mb-4 mb-md-0">
            <h3 style="margin-left: 10px;">Our Social Media</h3>
            <ul class="list-unstyled quick-info mb-4">
              <li class='d-flex flex-icon'>
                <i class="bi bi-instagram"></i>
                <a href="//instagram.com/jono_bojonegoro" class="d-flex align-items-center">@jono_bojonegoro</a>
              </li>
              <li class="d-flex flex-icon">
                <i class="bi bi-twitter"></i>
                <a href="//twitter.com/Desa_Jono" class="d-flex align-items-center">@Desa_Jono</a>
              </li>
              <li class="d-flex flex-icon">
                <span class="iconify" data-icon="fa-facebook-square" data-inline="false"></span>
                <a href="//www.facebook.com/profile.php?id=100070484598145" class="d-flex align-items-center">Jono Bojonegoro</a>
              </li>
              <li class="d-flex flex-icon">
                <span class="iconify" data-icon="websymbol:youtube" style="color: white;"></span>
                <a href="//www.youtube.com/channel/UCsozX6fPiLabnCmyWzQLBjA" class="d-flex align-items-center">Desa Jono Bojonegoro</a>
              </li>
            </ul>
          </div>


          <div class="col-md-3 mb-4 mb-md-0">
            <h3>Lokasi Desa</h3>
            <iframe id="google-maps"
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31659.233795830023!2d111.87805533946955!3d-7.308403045237198!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e782b7d00adffeb%3A0x943eb7313719dd0a!2sJono%2C%20Temayang%2C%20Kabupaten%20Bojonegoro%2C%20Jawa%20Timur!5e0!3m2!1sid!2sid!4v1625501419405!5m2!1sid!2sid" 
            width="250" height="250" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
            <div class="row">
              
            </div>
          </div>
          
          <div class="col-12">
            <div class="py-3 footer-menu-wrap d-md-flex align-items-center">
              <div class="site-logo-wrap ml-auto">
                <a href="#" class="site-logo">
                 Copyright 2021. Desa Jono, Temayang, East Java
                </a>
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </div>
  </footer>`

  
}


document.getElementById('footer').innerHTML = renderFooter();


