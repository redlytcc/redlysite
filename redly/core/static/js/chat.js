function initChat(csrf,us,Lasid) {
    Vue.http.headers.common['X-CSRFToken'] = csrf;
    if (localStorage.getItem("Stymenu")) {
        var menu = localStorage.getItem("Stymenu");
        if (menu == "Top") {
            document.getElementsByClassName('leftDiv')[0].style.display='none';
            document.getElementsByClassName('topDiv')[0].style.display='inherit';
            $(".rigthDiv").removeClass('lm');
        }
        else if (menu == "Left") {
            document.getElementsByClassName('leftDiv')[0].style.display='inherit';
            document.getElementsByClassName('topDiv')[0].style.display='none';
            $(".rigthDiv").addClass('lm');
        }
    }
    else{
        var menu = "Left"
    }
    if (localStorage.getItem("theme")) {
        var theme = localStorage.getItem("theme");
        if (theme == "MlPl") {
            $(".leftDiv").removeClass('d');
            $(".leftDiv").addClass('l');
            $(".topDiv").removeClass('d');
            $(".topDiv").addClass('l');
        }
        else if (theme == "MdPl") {
            $(".leftDiv").removeClass('l');
            $(".leftDiv").addClass('d');
            $(".topDiv").removeClass('l');
            $(".topDiv").addClass('d');
        }
    }
    else{
        var theme = "MlPl";
    }
    var app = new Vue({
        el: '.all',
        data:{
            ssc:menu,
            sst:theme,
            chatData:{'nome':us,'text':null},
            id:Lasid,
            cr:{},
            file: new FormData(),
            file2: ''
        },
        delimiters:['{$','$}'],
        mounted:function(){
            this.hel();
            console.log(this.id);
        },
        methods: {
            fileon:function(event){
                this.file2=event.target.files[0];
                this.file.append("img",event.target.files[0]);
                console.log(this.file);
            },
            hel:function() {
                this.$http.get('/apirest/getposts/'+this.id+'/')
                .then((rest)=>{
                    // console.log(rest);
                    this.cr=rest.body.u;
                    for (i in this.cr){
                        x=new Date(this.cr[i][4])
                        this.id=this.cr[i][0];
                        codigo  = '<div class="msm msm-'+this.cr[i][0]+'">';

                        if (this.cr[i][1] == us) {
                            codigo += '<span class="smsm" onclick="contentApp.del('+this.cr[i][0]+')" id="msm-'+this.cr[i][0]+'">>X<</span>';
                            codigo+='<div class="mymsm">';
                        }
                        else{
                            codigo+='<div class="another">';
                        }
                        codigo +=       '<h4>'+ this.cr[i][1] +'&nbsp;&nbsp;&nbsp;'+x.toDateString()+'</h4>'  	+
                                    '</div>';
                        if (this.cr[i][2]) {
                            codigo+="<img src='"+this.cr[i][2]+"' alt='imagem do usuario' title='imagem de redly' width='400' height='300'>";
                        }
                        if (this.cr[i][3] != 'null' && this.cr[i][3] != null) {
                            console.log(this.cr[i][3]);
                            codigo +=   '<div class="textinho">'	   +
                                    '<p><pre>'+ urlize(this.cr[i][3],nofollow=true) +'</pre></p>'     +
                                '</div>'							   +
                            '</div><br>';
                        }
                        $('#conv').prepend(codigo);
                    }

                })
                .catch((err)=>{
                    console.log('nothing');
                    console.log(err);

                });
                setTimeout(this.hel,1000);
            },
            sendChat:function() {
                this.file.append("nome",this.chatData.nome);
                this.file.append("text",this.chatData.text);

                this.$http.post('/apirest/postposts/',this.file)
                    .then((rest)=>{
                        // console.log(rest);
                        $('#formulario')[0].reset();
                        this.chatData={'nome':us,'text':null};
                        this.file=new FormData();
                        console.log(this.file);
                    })
                    .catch((err)=>{
                        // console.log(err);
                        this.chatData={'nome':us,'text':null};

                        this.file=new FormData();
                        console.log(this.file);
                    })
            },
            del:function(id) {

                this.$http.get('/redly/redid/'+id)
                    .then((rest)=>{
                        $(".msm-"+id).hide();
                    })
                    .catch((err)=>{
                        console.log(err);
                    })
            },
            goBack: function () {
                var leftDiv=this.$refs.left.style.width;
                var cl=document.querySelectorAll(".closeM");
                if(leftDiv == "5%"){
                    document.querySelector(".rigthDiv").style.width="85%";
                    document.querySelector(".rigthDiv").style.marginLeft="15%";
                    this.$refs.left.style.width="15%";
                    cl[1].style.display="none";
                    cl[0].style.display="block";
                }
                else{
                    this.$refs.left.style.width="5%";
                    document.querySelector(".rigthDiv").style.width="95%";
                    document.querySelector(".rigthDiv").style.marginLeft="5%";
                    cl[0].style.display="none";
                    cl[1].style.display="block";
                }
                console.log(document.getElementById("app").style.width);
            },
            chooseM:()=>{
                if($("select#menuS").val() == "Top"){
                    $(".rigthDiv").removeClass('lm');
                    document.getElementsByClassName('leftDiv')[0].style.display='none';
                    document.getElementsByClassName('topDiv')[0].style.display='inherit';
                    localStorage.setItem("Stymenu", "Top");
                }
                else if ($("select").val() == "Left") {
                    $(".rigthDiv").addClass('lm');
                    document.getElementsByClassName('leftDiv')[0].style.display='inherit';
                    document.getElementsByClassName('topDiv')[0].style.display='none';
                    localStorage.setItem("Stymenu", "Left");
                }
            },
            chooseT:()=>{
                if ($("select#theme").val() == "MlPl") {
                    $(".leftDiv").removeClass('d');
                    $(".leftDiv").addClass('l');
                    $(".topDiv").removeClass('d');
                    $(".topDiv").addClass('l');
                }
                else if ($("select#theme").val() == "MdPl") {
                    $(".leftDiv").removeClass('l');
                    $(".leftDiv").addClass('d');
                    $(".topDiv").removeClass('l');
                    $(".topDiv").addClass('d');
                }

            }
        }

    });
}
