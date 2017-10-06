$(document).ready(function(){
   $('#tmnt').hide().fadeIn(3000);

   $('button').click(function(){
        var color = $('input:text').val()
        if(color == 'blue'){
            $('img').slideUp(1000)
            $('#blue').fadeIn(3000)
            $('button').css('background-color', 'blue')
            $('button').css('color', 'white')
            $('h1').css('color', 'blue')
        } else if (color == 'red'){
            $('img').slideUp()
            $('#red').fadeIn(3000)
            $('button').css('background-color', 'red')
            $('button').css('color', 'white')
            $('h1').css('color', 'red')
        } else if (color == 'purple'){
            $('img').slideUp()
            $('#purple').fadeIn(3000)
            $('button').css('background-color', 'purple')
            $('button').css('color', 'white')
            $('h1').css('color', 'purple')
        } else if (color == 'orange'){
            $('img').slideUp()
            $('#orange').fadeIn(3000)
            $('button').css('background-color', 'orange')
            $('button').css('color', 'white')
            $('h1').css('color', 'orange')
        } else {
            $('img').slideUp()
            $('#april').fadeIn(3000)
        } 
   });


});