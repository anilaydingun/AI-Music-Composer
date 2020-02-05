function loading(){


    var x = document.getElementsByClassName("container");

    for (var i=0; i<x.length; i+=1) {
      x[i].style.display= 'none';
    }

    var col1 = document.getElementsByClassName('col-12')[0],
    newdiv1 = document.createElement('div');
    newdiv1.setAttribute("id","newid");
    newdiv1.setAttribute("class","container");
    //newdiv1.style.border = "solid #FFA07A";
    //newdiv1.innerHTML = "burak canbaz";
    newdiv1.style.setProperty("height","450px");
    newdiv1.style.setProperty("width","500px");
    // newdiv1.style.setAttribute("width","400px");
    //newdiv1.innerHTML = "burak"   
    //newdiv1.innerHTML = 'Music Features';
    newdiv1.style.fontSize = '16px';                
    col1.appendChild(newdiv1);

    var div1 = document.createElement('div');
    div1.setAttribute('id','div1');
    //div1.setAttribute('class','btn btn-primary');
    //div1.setAttribute('role','status');
    div1.innerHTML = "Loading...";
    div1.style.fontSize = "25px";
    div1.style.setProperty("margin-left","60px");
    div1.style.setProperty("height","160px");
    div1.style.setProperty("width","300px");
    newdiv1.appendChild(div1);

    var span = document.createElement('span');
    span.setAttribute('class','spinner-border spinner-border-sm');
    span.style.setProperty("height","150px");
    span.style.setProperty("width","150px");
    span.style.setProperty("margin-top","135px");
    // span.style.setProperty("margin-left","150px");
    //span.innerHTML = 'Loading';
    div1.appendChild(span);

     var span1 = document.createElement('span1');
     //span1.innerHTML = "Loading...";
     span.appendChild(span1);




}