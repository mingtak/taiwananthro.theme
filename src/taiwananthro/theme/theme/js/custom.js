$(document).ready(function(){
    $('.article-item .show-abs').click(function(){
        $(this).prev('.article-abs').slideToggle()
    })
/*
    $('#sc_li').click(function(){
        $(this).attr('class', 'active')
        if( $(this).attr('id') == 'tc_li'){
            $('#sc_li').attr('class', '')
        }else{
            $('#tc_li').attr('class', '')
        }
    })
*/
})

