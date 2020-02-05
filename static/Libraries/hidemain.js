function myFunction() {

    //var timesClicked=1;
    //var j;
    alert("myFunction");

    /*if(timesClicked%2===0){

        for(j=0; i<x.length; i++){
            x[j].style.display = 'none';
        }
    }*/

    //document.getElementById("hide").onclick = function() {
    //disable
    //this.disabled = true;

    //do some validation stuff
//}



   /* var col = document.getElementsByClassName('col-12')[0],
    newdiv = document.createElement('div');
    newdiv.setAttribute("id","newid");
    newdiv.setAttribute("class","container");
    newdiv.style.border = "solid #FFA07A";
    //newdiv.innerHTML = "burak canbaz";
    newdiv.style.setProperty("height","450px");
    newdiv.style.setProperty("width","500px");
    // newdiv.style.setAttribute("width","400px");
    //newdiv.innerHTML = "burak"   
    newdiv.innerHTML = 'Music Features';
    newdiv.style.fontSize = '16px';                
    col.appendChild(newdiv);  


    var i = 0;

    // var div3 = document.createElement('div');
    // //checkbox.type = "checkbox";
    // div3.name = "name";
    // div3.value = "value";
    // div3.className = "infos-ctn";
    // div3.id = "id" + i;
    // //div3.innerHTML= "Instrument 1";
    // div3.style.setProperty("height","100px");
    // div3.style.setProperty("width","470px");
    // newdiv.appendChild(div3);

    // var checkbox = document.createElement('input');
    // checkbox.type = 'checkbox';
    // checkbox.name = 'checkbox'+i;
    // checkbox.className = 'title';
    // checkbox.id = 'id' + i;
    // div3.appendChild(checkbox);
    // i++;

    // var checkbox1 = document.createElement('input');
    // checkbox1.type = 'checkbox';
    // checkbox1.name = 'checkbox'+i;
    // checkbox1.className = 'title';
    // checkbox1.id = 'id' + i;
    // div3.appendChild(checkbox1);
    // i++;

    // var checkbox2 = document.createElement('input');
    // checkbox2.type = 'checkbox';
    // checkbox2.name = 'checkbox'+i;
    // checkbox2.className = 'title';
    // checkbox2.id = 'id' + i;
    // div3.appendChild(checkbox2);
    // i++;


    // var checkbox3 = document.createElement('input');
    // checkbox3.type = 'checkbox';
    // checkbox3.name = 'checkbox'+i;
    // checkbox3.className = 'title';
    // checkbox3.id = 'id' + i;
    // div3.appendChild(checkbox3);
    // i++;

    // var checkbox4 = document.createElement('input');
    // checkbox4.type = 'checkbox';
    // checkbox4.name = 'checkbox'+i;
    // checkbox4.className = 'title';
    // checkbox4.id = 'id' + i;
    // div3.appendChild(checkbox4);
    // i++;


    


  //   for (var i = 0; i < 4; i++) {
  //     var label = document.createElement('label');
  //     var br = document.createElement('br');
  //     //var alabel = document.getElementById("<%=Label3.ClientID %>");
  //     var alabel = document.getElementById('div1');
  //     var last = alabel[alabel.length - 1];
  //     label.htmlFor = "lbl"+i;
  //     label.appendChild(Createcheckbox('test' + i));
  //     label.appendChild(document.createTextNode('RAJ1' + i));
  //     label.appendChild(br);
  //     //document.getElementById("<%=Label3.ClientID %>").appendChild(label);
  //  document.getElementById('newdiw').appendChild(label);
    // var div = document.createElement('div');
    // div.setAttribute("class","dropdown");
    // newdiv.appendChild(div);
    // var button = document.createElement('button');
    // button.setAttribute("class","btn btn-secondary dropdown-toggle");
    // button.type = 'button';
    // button.setAttribute("id","dropdownMenu2");
    // button.setAttribute("data-toggle","dropdown");
    // button.setAttribute("aria-haspopup","true");
    // button.setAttribute("aria-expanded","false");
    // div.appendChild(button);
    // var div1 = document.createElement('div');
    // div1.setAttribute("class","dropdown-menu");
    // div1.setAttribute("aria-labelledby","dropdownMenu2");
    // div.appendChild(div1);
    // var button1 = document.createElement('div');
    // button1.setAttribute("class","dropdown-item");
    // button1.type = 'button';
    // button1.innerHTML = "burak";
    // div1.appendChild(button1);


     var i, theContainer, theSelect, theOptions, numOptions, anOption;
     theOptions = ['Instrument 1','Instrument 2','Instrument 3','Instrument 4','Instrument 5'];
     var div3 = document.createElement('div');
     div3.setAttribute("class","infos-ctn");
     div3.style.setProperty("height","100px");
     div3.style.setProperty("width","470px");
     var select = document.createElement('select');
     select.name = 'name_of_select';
     select.id = 'id_of_select';
     select.setAttribute("class","timer");
     numOptions = theOptions.length;
     for (i = 0; i < numOptions; i++) {
         anOption = document.createElement('option');
         anOption.value = i;
         anOption.innerHTML = theOptions[i];
         select.appendChild(anOption);
     }
     div3.appendChild(select);
     newdiv.appendChild(div3);

    //  var i, theContainer, theSelect, theOptions, numOptions, anOption;
    //  theOptions = ['Instrument 1','Instrument 2','Instrument 3','Instrument 4','Instrument 5'];

    // //var div3 = document.getElementsByClassName('player-ctn');
    //  div3 = document.createElement('div');
    //  div3.setAttribute("id","div1");
    // //div3.setAttribute("class","infos-ctn");
    //  div3.setAttribute("class","infos-ctn");
    //  div3.style.setProperty("height","100px");
    //  div3.style.setProperty("width","470px");
    //  // div3.id = 'div1';
    //  // div3.className = 'btn-ctn';

    //  //theSelect = document.createElement('select');
    //  theSelect = document.createElement('select');
    //  theSelect.setAttribute("type","button");
    //  theSelect.setAttribute("class","browser-default custom-select");
    //  // theSelect.setAttribute("type","button");
    //  // theSelect.setAttribute("id","d");
    //  theSelect.name = 'name_of_select';
    //  //theSelect.type = 'button';
    //  theSelect.id = 'id_of_select';
    //  theSelect.className = 'class_of_select';
    //  numOptions = theOptions.length;
    //  for (i = 0; i < numOptions; i++) {
    //   anOption = document.createElement('option');
    //   anOption.value = i;
    //   anOption.innerHTML = theOptions[i];
    //   theSelect.appendChild(anOption);
    //  }
    // //document.getElementById('container_for_select_container').appendChild(div3);
    //  div3.appendChild(theSelect);
    
    //  newdiv.appendChild(div3);


    var index = 0;
   
    var div4 = document.createElement('div');
    div4.setAttribute("id","div2");
    div4.setAttribute("class","playlist-ctn");
    div4.innerHTML = "Features";
    newdiv.appendChild(div4);

    var innerdiv1 = document.createElement("div");
    innerdiv1.setAttribute("id","innerdiv-"+index);
    innerdiv1.setAttribute("class","playlist-track-ctn");
    innerdiv1.setAttribute("data-index", index);
    div4.appendChild(innerdiv1);
    

    var innerdiv2 = document.createElement("div");
    innerdiv2.setAttribute("id","innerdiv-"+index);
    innerdiv2.setAttribute("class","playlist-btn-play");
    innerdiv2.innerHTML = "Velocity";
    innerdiv1.appendChild(innerdiv2);
  

    var innercheckbox1 = document.createElement('input');
    innercheckbox1.type = 'radio';
    innercheckbox1.setAttribute("onclick","check()");
    innercheckbox1.name = 'radio'+index;
    innercheckbox1.className = 'title';
    innercheckbox1.value = "None";
    innercheckbox1.id = 'id' + index;
    innerdiv1.appendChild(innercheckbox1);
    index++;


    var innercheckbox2= document.createElement('input');
    innercheckbox2.type = 'radio';
    innercheckbox2.name = 'radio'+index;
    innercheckbox1.className = 'title';
    innercheckbox2.id = 'id' + index;
    innerdiv1.appendChild(innercheckbox2);
    index++;

    var innerdiv3 = document.createElement("div");
    innerdiv3.setAttribute("id","innerdiv-"+index);
    innerdiv3.setAttribute("class","playlist-track-ctn");
    innerdiv3.setAttribute("data-index", index);
    div4.appendChild(innerdiv3);

    var innerdiv4 = document.createElement("div");
    innerdiv4.setAttribute("id","innerdiv-"+index);
    innerdiv4.setAttribute("class","playlist-btn-play");
    innerdiv4.innerHTML = "Length  ";
    innerdiv3.appendChild(innerdiv4);
    index+=1;

    var innercheckbox3 = document.createElement('input');
    innercheckbox3.type = 'radio';
    innercheckbox3.name = 'radio'+index;
    innercheckbox3.className = 'title';
    innercheckbox3.id = 'id' + index;
    innerdiv3.appendChild(innercheckbox3);
    index++;

    var innercheckbox4 = document.createElement('input');
    innercheckbox4.type = 'radio';
    innercheckbox4.name = 'radio'+index;
    //innercheckbox4.className = 'title';
    innercheckbox4.id = 'id' + index;
    innerdiv3.appendChild(innercheckbox4);
    index++;

    var innerdiv5 = document.createElement("div");
    innerdiv5.setAttribute("id","innerdiv-"+index);
    innerdiv5.setAttribute("class","playlist-track-ctn");
    innerdiv5.setAttribute("data-index", index);
    div4.appendChild(innerdiv5);
    

    var innerdiv6 = document.createElement("div");
    innerdiv6.setAttribute("id","innerdiv-"+index);
    innerdiv6.setAttribute("class","playlist-btn-play");
    innerdiv6.innerHTML = "Wait";
    innerdiv5.appendChild(innerdiv6);
    index+=1;

    var innercheckbox5 = document.createElement('input');
    innercheckbox5.type = 'radio';
    innercheckbox5.name = 'radio'+index;
    innercheckbox5.className = 'title';
    innercheckbox5.id = 'id' + index;
    innerdiv5.appendChild(innercheckbox5);
    index++;

    var innercheckbox6 = document.createElement('input');
    innercheckbox6.type = 'radio';
    innercheckbox6.name = 'radio'+index;
    //innercheckbox6.className = 'title';
    innercheckbox6.id = 'id' + index;
    innerdiv5.appendChild(innercheckbox6);
    index++;

    var innerdiv7 = document.createElement("div");
    innerdiv7.setAttribute("id","innerdiv-"+index);
    innerdiv7.setAttribute("class","custom-button");
    innerdiv7.setAttribute("data-index", index);
    div4.appendChild(innerdiv7);
    

    var innerdiv8 = document.createElement("button");
    innerdiv8.setAttribute("id","innerdiv-"+index);
    //innerdiv8.backgroundColor = "blue";
    innerdiv8.setAttribute("class","btn btn-outline-danger btn-lg");
    innerdiv8.style.textAlign = "center";
    innerdiv8.setAttribute("onclick","loading()");
    //innerdiv8.setAttribute("height","50");
    //innerdiv8.setAttribute("width","350");
    innerdiv8.innerHTML = "Generate";
    innerdiv7.appendChild(innerdiv8);
    index+=1;

*/
    



  }
