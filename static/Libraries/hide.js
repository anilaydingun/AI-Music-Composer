 function hide() {

    var hide = document.getElementsByClassName("content")[0];


    for (var i=0; i<hide.length; i+=1) {
      hide[i].style.display= 'block';
    }
     /*(var x = document.getElementsByClassName("player-ctn");
     for (var i=0; i<x.length; i+=1) {
       x[i].style.display= 'none';
    
   }
    var col = document.getElementsByClassName('col-12')[0],
    newdiv = document.createElement('div');
    newdiv.setAttribute("id","newid");
    newdiv.setAttribute("class","player-ctn"); 
    //newdiv.innerHTML = "burak"                    
    col.appendChild(newdiv);                 
    //section.insertBefore(newdiv,section.firstChild) 

    // var div1 = document.getElementsByClassName('player-ctn');
    // div1 = document.createElement('div');
    // div1.id = 'innerdiv1';
    // div1.className = 'infos-ctn';
    // //div1.innerHTML = "burak";
    // newdiv.appendChild(div1);

    

    // var div2 = document.getElementsByClassName('player-ctn');
    // div2 = document.createElement('div');
    // div2.id = 'innerdiv2';
    // div2.className = 'infos-ctn';
    // //div2.innerHTML = "burak";
    // newdiv.appendChild(div2);

    var i, theContainer, theSelect, theOptions, numOptions, anOption;
    theOptions = ['Instrument 1','Instrument 2','Instrument 3','Instrument 4','Instrument 5'];

    var div3 = document.getElementsByClassName('player-ctn');
    div3 = document.createElement('div');
    div3.setAttribute("id","div1");
    div3.setAttribute("class","infos-ctn")
    // div3.id = 'div1';
    // div3.className = 'btn-ctn';

    theSelect = document.createElement('select');
    theSelect.name = 'name_of_select';
    //theSelect.type = 'button';
    theSelect.id = 'id_of_select';
    theSelect.className = 'class_of_select';
    numOptions = theOptions.length;
    for (i = 0; i < numOptions; i++) {
     anOption = document.createElement('option');
     anOption.value = i;
     anOption.innerHTML = theOptions[i];
     theSelect.appendChild(anOption);
    }
    //document.getElementById('container_for_select_container').appendChild(div3);
    div3.appendChild(theSelect);
    
    newdiv.appendChild(div3);

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
    index+=1;

    var innerdiv3 = document.createElement("div");
    innerdiv3.setAttribute("id","innerdiv-"+index);
    innerdiv3.setAttribute("class","playlist-track-ctn");
    innerdiv3.setAttribute("data-index", index);
    div4.appendChild(innerdiv3);
    

    var innerdiv4 = document.createElement("div");
    innerdiv4.setAttribute("id","innerdiv-"+index);
    innerdiv4.setAttribute("class","playlist-btn-play");
    innerdiv4.innerHTML = "Length";
    innerdiv3.appendChild(innerdiv4);
    index+=1;

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

    

    // var div4 = document.getElementsByClassName('player-ctn');
    // div4 = document.createElement('div');
    // div4.id = 'div2';
    // div4.className = 'playlist-ctn';
    // div4.innerHTML = "Features";
    // newdiv.appendChild(div4);
    

    // var innerdiv1 = document.getElementsByClassName('playlist-ctn');
    // innerdiv1 = document.createElement('div');
    // innerdiv1.id = 'innerdiv1';
    // innerdiv1.className = 'playlist-track-ctn';
    // //innerdiv1.innerHTML = "";
    // div4.appendChild(innerdiv1);

    // var innerdiv2 = document.getElementsByClassName('playlist-track-ctn');
    // innerdiv2 = document.createElement('div');
    // innerdiv2.id = 'innerdiv2';
    // innerdiv2.className = 'playlist-btn-play';
    // innerdiv2.innerHTML = "Velocity";
    // innerdiv1.appendChild(innerdiv2);


//     var div5 = document.getElementsByClassName('player-ctn');
//     div5 = document.createElement('div');
//     div5.id = 'div3';
//     div5.className = 'playlist-ctn';
//     newdiv.appendChild(div5);

//     var innerdiv1 = document.getElementsByClassName('playlist-ctn');
//     innerdiv1 = document.createElement('div');
//     innerdiv1.id = 'innerdiv1';
//     innerdiv1.className = 'playlist-track-ctn';
//     //innerdiv1.innerHTML = "";
//     div5.appendChild(innerdiv1);

//     var innerdiv2 = document.getElementsByClassName('playlist-track-ctn');
//     innerdiv2 = document.createElement('div');
//     innerdiv2.id = 'innerdiv2';
//     innerdiv2.className = 'playlist-btn-play';
//     innerdiv2.innerHTML = "Length";
//     innerdiv1.appendChild(innerdiv2);

//     for (var i = 0; i < 100; i++) {
//         createTrackItem(i);
    
//  }

 }


//  var i, theContainer, theSelect, theOptions, numOptions, anOption;
//  theOptions = ['option 1','option 2','option 3'];
 
//  // Create the container <div>
//  theContainer = document.createElement('div');
//  theContainer.id = 'my_new_div';
 
//  // Create the <select>
//  theSelect = document.createElement('select');
 
//  // Give the <select> some attributes
 
 
//  // Define something to do onChange
//  theSelect.onchange = function () {
//      // Do whatever you want to do when the select changes
//      alert('You selected option '+this.selectedIndex);
//  };
 
//  // Add some <option>s
 
 
 
 // Add the <div> to the DOM, then add the <select> to the <div>*/
 }