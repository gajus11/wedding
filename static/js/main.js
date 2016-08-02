//Submit form on submit
$('#rsvp-form').on('submit', function(event){
    event.preventDefault();
    submit_form();
});

function submit_form(){
    var transport = false;
    if($('#id_transport').is(":checked")){
        transport = true;
    }

    var accomodation = false;
    if($('#id_accomodation').is(":checked")){
        accomodation = true;
    }

    $.ajax({
        url : 'rsvp/create_rsvp/',
        type : 'POST',
        data : {
            'name' : $('#id_name').val(),
            'last_name' : $('#id_last_name').val(),
            'adults_number' :  $('#id_adults_number').val(),
            'childrens_number' :  $('#id_childrens_number').val(),
            'transport' :  transport,
            'accomodation' :  accomodation
        },

        success : function(json) {
            $('.panel-body').html(
                '<h4 class="text-center">Dziękujemy za potwierdzenie swojej obecności. Do zobaczenia!</h4>'
            );
        },

        error : function(xhr,errmsg,err) {
            var errors = JSON.parse(xhr.responseJSON.errors)
            for(var key in errors){
                var id = '#id_' + key;
                $(id).addClass('form-error');
            }
        },
    });
};

$(function() {

    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});