$(document).ready(function(){
// colorbox

$("body.section-photopraphy #content-core img").click(function(){
    $("body.section-photopraphy #content-core img")
        .colorbox({html:this.outerHTML})
})


/*    $('.article-item .show-abs').click(function(){
        $(this).prev('.article-abs').slideToggle()
    })
*/
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

