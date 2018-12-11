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

if (localStorage.getItem("StymenuL")) {
    var cl=document.querySelectorAll(".closeM");
    if (localStorage.getItem("StymenuL") == "5%") {
        document.querySelector(".rigthDiv").style.width="95%";
        document.querySelector(".rigthDiv").style.marginLeft="5%";
        document.querySelector(".leftDiv").style.width="5%";
        cl[0].style.display="none";
        cl[1].style.display="block";
    }
    else{
        document.querySelector(".rigthDiv").style.width="85%";
        document.querySelector(".rigthDiv").style.marginLeft="15%";
        document.querySelector(".leftDiv").style.width="15%";
        cl[1].style.display="none";
        cl[0].style.display="block";

    }
}
var app = new Vue({
    el: '.all',
    data:{
        ssc:menu,
        sst:theme,
    },
    delimiters:['{$','$}'],
    methods: {
        goBack: function () {
            var leftDiv=this.$refs.left.style.width;
            var cl=document.querySelectorAll(".closeM");
            if(leftDiv == "5%"){
                document.querySelector(".rigthDiv").style.width="85%";
                document.querySelector(".rigthDiv").style.marginLeft="15%";
                this.$refs.left.style.width="15%";
                cl[1].style.display="none";
                cl[0].style.display="block";
                localStorage.setItem("StymenuL","15%");
            }
            else{
                this.$refs.left.style.width="5%";
                document.querySelector(".rigthDiv").style.width="95%";
                document.querySelector(".rigthDiv").style.marginLeft="5%";
                cl[0].style.display="none";
                cl[1].style.display="block";
                localStorage.setItem("StymenuL","5%");

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
                localStorage.setItem("theme", "MlPl");
            }
            else if ($("select#theme").val() == "MdPl") {
                $(".leftDiv").removeClass('l');
                $(".leftDiv").addClass('d');
                $(".topDiv").removeClass('l');
                $(".topDiv").addClass('d');
                localStorage.setItem("theme", "MdPl");
            }
        }
    }
});
