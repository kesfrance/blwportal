$(document).ready(function(){
    $(".mainmenu li, #myNavbar ul li").click(function(){
        $(this).addClass('activemode').siblings().removeClass('activemode');
    });
    
    $('#myNavbar ul li').click(function(){
        $(this).addClass('activemode').siblings().removeClass('activemode');
        $('.navbar-toggle').click();
        
    });
    
    $('#loginerror').css({'color': 'red', 'margin-top':'5px'});
});