var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";
document.head.appendChild(script);


script.onload = function() {
    tinymce.init({
        selector: '#id_body',
        height: 1000,
        plugins: [
            'advlist autolink link image lists charmap print preview hr anchor pagebreak',
            'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
            'table emoticons template paste help', 'codesample'
        ],
        toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
            'bullist numlist outdent indent | link image | print preview media fullscreen | ' +
            'forecolor backcolor emoticons | help' +
            'codesample',
        menu: {
            favs: { title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons' }
        },
        menubar: 'favs file edit view insert format tools table help',
        content_css: 'css/content.css',
        valid_elements: "@[id|class|style|title|dir<ltr?rtl|lang|xml::lang|onclick|ondblclick|" +
            "onmousedown|onmouseup|onmouseover|onmousemove|onmouseout|onkeypress|" +
            "onkeydown|onkeyup],a[rel|rev|charset|hreflang|tabindex|accesskey|type|" +
            "name|href|target|title|class|onfocus|onblur],strong/b,em/i,strike,u," +
            "#p,-ol[type|compact],-ul[type|compact],-li,br,img[longdesc|usemap|" +
            "src|border|alt=|title|hspace|vspace|width|height|align],-sub,-sup," +
            "-blockquote,-table[border=0|cellspacing|cellpadding|width|frame|rules|" +
            "height|align|summary|bgcolor|background|bordercolor],-tr[rowspan|width|" +
            "height|align|valign|bgcolor|background|bordercolor],tbody,thead,tfoot," +
            "#td[colspan|rowspan|width|height|align|valign|bgcolor|background|bordercolor" +
            "|scope],#th[colspan|rowspan|width|height|align|valign|scope],caption,-div," +
            "-span,-code,-pre,address,-h1,-h2,-h3,-h4,-h5,-h6,hr[size|noshade],-font[face" +
            "|size|color],dd,dl,dt,cite,abbr,acronym,del[datetime|cite],ins[datetime|cite]," +
            "object[classid|width|height|codebase|*],param[name|value|_value],embed[type|width" +
            "|height|src|*],script[src|type],map[name],area[shape|coords|href|alt|target],bdo," +
            "button,col[align|char|charoff|span|valign|width],colgroup[align|char|charoff|span|" +
            "valign|width],dfn,fieldset,form[action|accept|accept-charset|enctype|method]," +
            "input[accept|alt|checked|disabled|maxlength|name|readonly|size|src|type|value]," +
            "kbd,label[for],legend,noscript,optgroup[label|disabled],option[disabled|label|selected|value]," +
            "q[cite],samp,select[disabled|multiple|name|size],small," +
            "textarea[cols|rows|disabled|name|readonly],tt,var,big," +
            "iframe[src|title|width|height|allowfullscreen|frameborder]",
        codesample_languages: [
            { text: 'HTML/XML', value: 'markup' },
            { text: 'JavaScript', value: 'javascript' },
            { text: 'CSS', value: 'css' },
            { text: 'PHP', value: 'php' },
            { text: 'Ruby', value: 'ruby' },
            { text: 'Python', value: 'python' },
            { text: 'Java', value: 'java' },
            { text: 'C', value: 'c' },
            { text: 'C#', value: 'csharp' },
            { text: 'C++', value: 'cpp' }
        ],
    });
}