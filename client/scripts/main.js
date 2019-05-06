// Global Variables

// Buttons
var searchButton;
var filterButton;
var resetButton;
var prevButton;
var nextButton;

//sliders
var lowCostRange;
var highCostRange;

var lowCost = "0";
var highCost = "30";

var lowHealthRange;
var highHealthRange;

var lowHealth = "0";
var highHealth = "25";

var lowAttackRange;
var highAttackRange;

var lowAttack = "0";
var highAttack = "25";

//slider labels
var lowCostText;
var highCostText;

var lowHealthText;
var highHealthText;

var lowAttackText;
var highAttackText;

// radio buttons
var typeButton;
var classButton;
var rarityButton;

// dictionaries
var typeDict;
var classDict;
var rarityDict;
var costDict;
var attDict;
var heaDict;

// boxes
var searchBox;

// Card Images
var card1;
var card2;
var card3;
var card4;
var card5;
var card6;
var card7;
var card8;
var card9;
var card10;
var cardList;
var baseURL= "http://127.0.0.1:8080/"
var defaultURL="http://media-hearth.cursecdn.com/attachments/2/105/cardback-promotional.png"
var pageNum=1;

var currentCards = [];

window.onload = function(){
	// Get all the elements we need by ID
	
	// Get Buttons
	searchButton=document.getElementById("searchButton")
    prevButton=document.getElementById("prevButton")
	nextButton=document.getElementById("nextButton")
	filterButton=document.getElementById("filterButton")
	resetButton=document.getElementById("resetButton")

	//Search Box
	searchBox=document.getElementById("nameBox")

	//Sliders
	lowCostRange=document.getElementById("lowCostRange")
	highCostRange= document.getElementById("highCostRange")
	
	lowCostText=document.getElementById("lowCostText")
	highCostText=document.getElementById("highCostText")

	lowHealthRange= document.getElementById("lowHealthRange")
	highHealthRange= document.getElementById("highHealthRange")

	lowHealthText=document.getElementById("lowHealthText")
    highHealthText=document.getElementById("highHealthText")

	lowAttackRange= document.getElementById("lowAttackRange")
	highAttackRange= document.getElementById("highAttackRange")
	
	lowAttackText=document.getElementById("lowAttackText")
    highAttackText=document.getElementById("highAttackText")

	// Get all the card image elements and put them in a list       
    card1=document.getElementById("card1")
    card2=document.getElementById("card2")
    card3=document.getElementById("card3")
    card4=document.getElementById("card4")
    card5=document.getElementById("card5")
    card6=document.getElementById("card6")
    card7=document.getElementById("card7")
    card8=document.getElementById("card8")
    card9=document.getElementById("card9")
    card10=document.getElementById("card10")
    cardList=[card1,card2,card3,card4,card5,card6,card7,card8,card9,card10];

	// Add event listeners
	searchButton.onclick=function send(){getCardsByName()}
    
    //goes to the previous "page" of cards to display the previous group of 10
    prevButton.addEventListener('click', function() {
  		pageNum=pageNum-10
		displayCards(currentCards)
	});

	//advances the "page" of cards to display the next group of up to 10
	nextButton.addEventListener('click', function() {
        pageNum=pageNum+10
		displayCards(currentCards)
    });
	
	//calls get functions to set type, class, and rarity variables, then
	//calls the getCardsByType() function to start the filter process
	filterButton.addEventListener('click', function() {
		pageNum = 0
		getType()
		getClass()
		getRarity()
		getCardsByType()
	});

	//resets card display, slider range/value, and radio buttons to
	//default settings
	resetButton.addEventListener('click', function() {
		lowCostRange.value=0
		highCostRange.value=30
		lowAttackRange.value=0
		highAttackRange.value=25
		lowHealthRange.value=0
		highHealthRange.value=25
		
		lowCostText.innerHTML=lowCostRange.value
		highCostText.innerHTML=highCostRange.value
		lowAttackText.innerHTML=lowAttackRange.value
		highAttackText.innerHTML=highAttackRange.value
		lowHealthText.innerHTML=lowHealthRange.value
		highHealthText.innerHTML=highHealthRange.value
		
		document.getElementById("Allt").checked = true
		document.getElementById("Druid").checked = true
		document.getElementById("Free").checked = true
		
		currentCards = []
		displayCards(currentCards)
	});

	// Sliders
	lowCostRange.addEventListener('change', function(){

		if(parseInt(lowCostRange.value) > parseInt(highCostRange.value)){
			lowCostRange.value=highCostRange.value;
		}
		lowCostText.innerHTML=lowCostRange.value;
		lowCost=lowCostRange.value
	});

	highCostRange.addEventListener('change', function(){

		if(parseInt(lowCostRange.value) > parseInt(highCostRange.value)){
                        highCostRange.value=lowCostRange.value;
                }

        highCostText.innerHTML=highCostRange.value;
		highCost=highCostRange.value
	});
	lowHealthRange.addEventListener('change', function(){
	
		if(parseInt(lowHealthRange.value) > parseInt(highHealthRange.value)){
                        lowHealthRange.value=highHealthRange.value;
                }

        lowHealthText.innerHTML=lowHealthRange.value;
		lowHealth=lowHealthRange.value
	});

    highHealthRange.addEventListener('change', function(){
    
		if(parseInt(lowHealthRange.value) > parseInt(highHealthRange.value)){
                        highHealthRange.value=lowHealthRange.value;
                }
        highHealthText.innerHTML=highHealthRange.value;
		highHealth=highHealthRange.value
	});
	
	lowAttackRange.addEventListener('change', function(){
	
		if(parseInt(lowAttackRange.value) > parseInt(highAttackRange.value)){
                        lowAttackRange.value=highAttackRange.value;
                }
                
        lowAttackText.innerHTML=lowAttackRange.value;
		lowAttack=lowAttackRange.value;
	});

    highAttackRange.addEventListener('change', function(){

		if( parseInt(lowAttackRange.value) > parseInt(highAttackRange.value)){
                        highAttackRange.value=lowAttackRange.value;
                }
        highAttackText.innerHTML=highAttackRange.value;
		highAttack=highAttackRange.value
	});

	
}

//This function parses all six dictionaries included within the filter function
//(type, class, rarity, cost, attack, and health) and finishes with a list of all
//cards that are common among all lists (four lists for spells/all, six for
//minions). This list is passed to displayCards(), which outputs it
function combineDicts() 
{
	currentCards = []
	var found = false
	
	//iterates through the type dictionary
	for (card in typeDict) {
		found = false
		//iterates through the class dictionary
		for (card1 in classDict) {
			if (classDict[card1]["dbfId"] == typeDict[card]["dbfId"]) {
				found = true
				break
			}
		}
		if (found) {
			found = false
			//iterates through the rarity dictionary
			for (card2 in rarityDict) {
				if (rarityDict[card2]["dbfId"] == typeDict[card]["dbfId"]) {
					found = true
					break
				}
			}
			if (found) {
				found = false
				//iterates through the cost dictionary
				for (card3 in costDict) {
					if (costDict[card3]["dbfId"] == typeDict[card]["dbfId"]) {
						found = true
						break
					}
				}
				//looking for "all" or "minions"
				if (found && typeButton != "spells") {
					//if card is spell but user searching for all, adds to 
					//the net dict
					if (typeDict[card]["type"] == "SPELL") {
						currentCards.push(typeDict[card])
					}
					//card is a minion
					else {
						found = false
						//iterates through attack dictionary
						for (card4 in attDict) {
							if (attDict[card4]["dbfId"] == typeDict[card]["dbfId"]) {
								found = true
								break
							}
						}
						if (found) {
							found = false
							for (card5 in heaDict) {
								//iterates through health dictionary
								if (heaDict[card5]["dbfId"] == typeDict[card]["dbfId"]) {
									found = true
									currentCards.push(typeDict[card])
									break
								}
							}
						}
						else {
							continue
						}
					}
				}
				//looking for "spells"
				else if (found && (typeButton == "spells")) 
				{
					currentCards.push(typeDict[card])
				}
				//"continue"s here and below indicate the for loop should advance
				else {
					continue
				}
			}
			else {
				continue
			}
		}
		else {
			continue
		}
	}
	
	displayCards(currentCards)
}

//makes a get request to the web server, which returns a list of cards of a 
//specified type
function getCardsByType(){
	console.log("Searching for: ")
	console.log(typeButton)
	
	var xhr = new XMLHttpRequest()
	
	if (typeButton != "ALL") {
		xhr.open("GET", baseURL+typeButton+"/", true)
		
		xhr.onload = function(e) {
			myResponse=JSON.parse(xhr.responseText);
			typeDict=myResponse[typeButton]
			getCardsByClass()
		}
	}
	else {
		xhr.open("GET", baseURL+"cards/", true)
		
		xhr.onload = function(e) {
			myResponse=JSON.parse(xhr.responseText);
			typeDict=myResponse["cards"]
			getCardsByClass()
		}
	}
	xhr.send(null)
}

//makes a get request to the web server, which returns a list of cards of a 
//specified class
function getCardsByClass(){
	console.log("Searching for: ")
	console.log(classButton)
	
	var xhr = new XMLHttpRequest()
	
	if (classButton != "ALL") {
		xhr.open("GET", baseURL+"cards/class/"+classButton, true)
	}
	else {
		xhr.open("GET", baseURL+"cards/", true)
	}
	xhr.onload = function(e) {
		var myResponse=JSON.parse(xhr.responseText);
		classDict=myResponse["cards"]
		getCardsByRarity()
	}
	xhr.send(null)
}

//makes a get request to the web server, which returns a list of cards of a
//specified rarity
function getCardsByRarity() {
	console.log("Searching for: ")
	console.log(rarityButton)
	
	var xhr = new XMLHttpRequest()
	
	if (rarityButton != "ALL") {
		xhr.open("GET", baseURL+"cards/rarity/"+rarityButton, true)
	}
	else {
		xhr.open("GET", baseURL+"cards/", true)
	}
	xhr.onload = function(e) {
		var myResponse=JSON.parse(xhr.responseText);
		rarityDict=myResponse["cards"]
		getCardsByCost()
	}
	xhr.send(null)
}

//makes a get request to the web server, which returns a list of cards that 
//fall within a certain cost range
function getCardsByCost() {
	console.log("Searching for: ")
	console.log(lowCost, " ", highCost)
	
	if (lowCost.length < 2) {
		lowCost = "0" + lowCost
	}
	if (highCost.length < 2) {
		highCost = "0" + highCost
	}
	
	var xhr = new XMLHttpRequest()
	xhr.open("GET", baseURL+"cards/cost/"+lowCost+highCost, true)
	
	xhr.onload = function(e) {
		var myResponse=JSON.parse(xhr.responseText);
		costDict=myResponse["cards"]
		getCardsByAttack()
	}
	xhr.send(null)	
}

//makes a get request to the web server, which returns a list of cards that
//fall within a certain attack range
function getCardsByAttack() {
	console.log("Searching for: ")
	console.log(lowAttack, " ", highAttack)
	
	if (lowAttack.length < 2) {
		lowAttack = "0" + lowAttack
	}
	if (highAttack.length < 2) {
		highAttack = "0" + highAttack
	}
	
	var xhr = new XMLHttpRequest()
	xhr.open("GET", baseURL+"minions/attack/"+lowAttack+highAttack, true)
	
	xhr.onload = function(e) {
		var myResponse=JSON.parse(xhr.responseText);
		attDict=myResponse["minions"]
		getCardsByHealth()
	}
	xhr.send(null)
}

//makes a get request to the web server, which returns a list of cards that
//fall within a certain health range
function getCardsByHealth() {
	console.log("Searching for: ")
	console.log(lowHealth, " ", highHealth)

	if (lowHealth.length < 2) {
		lowHealth = "0" + lowHealth
	}
	if (highHealth.length < 2) {
		highHealth = "0" + highHealth
	}
	
	var xhr = new XMLHttpRequest()
	xhr.open("GET", baseURL+"minions/health/"+lowHealth+highHealth, true)
	
	xhr.onload = function(e) {
		var myResponse=JSON.parse(xhr.responseText);
		heaDict=myResponse["minions"]
		combineDicts()
	}
	xhr.send(null)
}

//makes a get request to the web server, which returns a list of cards that
//contain a desired string in their name
function getCardsByName(){
        // Clear Card
        for (card in cardList){
            cardList[card].src=defaultURL
        }
        
        pageNum=0;

	console.log("Searching for: ")
        console.log(searchBox.value)
        NAME=searchBox.value
        var xhr = new XMLHttpRequest()

        xhr.open("GET", baseURL+"cards/name/"+NAME, true)
        xhr.onload = function(e){
		var myResponse=JSON.parse(xhr.responseText);
                currentCards=myResponse["cards"]
                displayCards(currentCards)
	}
	xhr.send(null)
}

//updates the src and alt of the ten image elements in the HTML and displays
//the cards to the user
function displayCards(cards){

    for (card in cardList){
        cardList[card].src=defaultURL
    }

	card1 = document.getElementById("card1")
	card1.src= cards[pageNum]["url"]
	card1.alt= cards[pageNum]["name"]
	card2 = document.getElementById("card2")
	card2.src= cards[pageNum+1]["url"]
	card2.alt= cards[pageNum+1]["name"]
	card3 = document.getElementById("card3")
	card3.src= cards[pageNum+2]["url"]
	card3.alt= cards[pageNum+2]["name"]
	card4 = document.getElementById("card4")
	card4.src= cards[pageNum+3]["url"]
	card4.alt= cards[pageNum+3]["name"]
	card5 = document.getElementById("card5")
	card5.src= cards[pageNum+4]["url"]
	card5.alt= cards[pageNum+4]["name"]
	card6 = document.getElementById("card6")
	card6.src= cards[pageNum+5]["url"]
	card6.alt= cards[pageNum+5]["name"]
	card7 = document.getElementById("card7")
	card7.src= cards[pageNum+6]["url"]
	card7.alt= cards[pageNum+6]["name"]
	card8 = document.getElementById("card8")
	card8.src= cards[pageNum+7]["url"]
	card8.alt= cards[pageNum+7]["name"]
	card9 = document.getElementById("card9")
	card9.src= cards[pageNum+8]["url"]
	card9.alt= cards[pageNum+8]["name"]
	card10 = document.getElementById("card10")
	card10.src= cards[pageNum+9]["url"]
	card10.alt= cards[pageNum+9]["name"]

}

//sets the typeButton variable equal to whatever radio button is checked in
//the type group
function getType() {
	if (document.getElementById("Allt").checked == true) {
		typeButton = "ALL"
	}
	else if (document.getElementById("Minions").checked == true) {
		typeButton = "minions"
	}
	else if (document.getElementById("Spells").checked == true) {
		typeButton = "spells"
	}
}

//sets the classButton variable equal to whatever radio button is checked in
//the class group
function getClass() {
	if (document.getElementById("Druid").checked == true) {
		classButton = "DRUID"
	}
	if (document.getElementById("Hunter").checked == true) {
		classButton = "HUNTER"
	}
	if (document.getElementById("Mage").checked == true) {
		classButton = "MAGE"
	}
	if (document.getElementById("Paladin").checked == true) {
		classButton = "PALADIN"
	}
	if (document.getElementById("Priest").checked == true) {
		classButton = "PRIEST"
	}
	if (document.getElementById("Rogue").checked == true) {
		classButton = "ROGUE"
	}
	if (document.getElementById("Shaman").checked == true) {
		classButton = "SHAMAN"
	}
	if (document.getElementById("Warlock").checked == true) {
		classButton = "WARLOCK"
	}
	if (document.getElementById("Warrior").checked == true) {
		classButton = "WARRIOR"
	}
	if (document.getElementById("Allc").checked == true) {
		classButton = "ALL"
	}
}

//sets the rarityButton variable equal to whatever radio button is checked in
//the rarity group
function getRarity() {
	if (document.getElementById("Free").checked == true) {
		rarityButton = "FREE"
	}
	if (document.getElementById("Common").checked == true) {
		rarityButton = "COMMON"
	}
	if (document.getElementById("Rare").checked == true) {
		rarityButton = "RARE"
	}
	if (document.getElementById("Epic").checked == true) {
		rarityButton = "EPIC"
	}
	if (document.getElementById("Legendary").checked == true) {
		rarityButton = "LEGENDARY"
	}
	if (document.getElementById("Allr").checked == true) {
		rarityButton = "ALL"
	}
}
