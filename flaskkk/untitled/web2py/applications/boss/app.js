/**
 * Created by feng.qian on 2016/5/12.
 */
var stage = new createjs.Stage("gameview");

createjs.Ticker.setFPS(30);
createjs.Ticker.addEventListener("tick",stage);

var gameview = new createjs.Container();

gameview.x = 35;
gameview.y = 35;

stage.addChild(gameview);

var circleArr = [[],[],[],[],[],[],[],[],[]];
var currentCat ;



function circleClick(event) {
    if (event.target.getCircleType() != Circle.TYPE_CAT) {
        event.target.setCircleType(Circle.TYPE_SELECT);

    }

    if (currentCat.indexX==0 ||currentCat.indexX==8 ||currentCat.indexY==0 ||currentCat.indexY==8){
        alert("game over");
        return;
    }

    var leftCircle = circleArr[ currentCat.indexX -1 ][ currentCat.indexY ];
    var rightCircle = circleArr[currentCat.indexX +1 ][currentCat.indexY];
    var lefttopCircle = circleArr[currentCat.indexX -1 ][currentCat.indexY-1];
    var righttopCircle = circleArr[currentCat.indexX  ][currentCat.indexY -1];
    var leftbottomCircle = circleArr[currentCat.indexX -1 ][currentCat.indexY+1];
    var rightbottomCircle = circleArr[currentCat.indexX  ][currentCat.indexY +1];
    if (leftCircle.getCircleType()==1){
        leftCircle.setCircleType(3);
        currentCat.setCircleType(1);
        currentCat = leftCircle;
    }else

       if (rightCircle.getCircleType()==1){
        rightCircle.setCircleType(3);
        currentCat.setCircleType(1);
        currentCat = rightCircle;
    }else
         if (lefttopCircle.getCircleType()==1){
        lefttopCircle.setCircleType(3);
        currentCat.setCircleType(1);
        currentCat = lefttopCircle;
    }else
         if (righttopCircle.getCircleType()==1){
        righttopCircle.setCircleType(3);
        currentCat.setCircleType(1);
        currentCat = righttopCircle;
    }else
         if (leftbottomCircle.getCircleType()==1){
        leftbottomCircle.setCircleType(3);
        currentCat.setCircleType(1);
        currentCat = leftbottomCircle;
    }else
         if (rightbottomCircle.getCircleType()==1){
        rightbottomCircle.setCircleType(3);
        currentCat.setCircleType(1);
        currentCat = rightbottomCircle;
    }else{
             alert("you win");
         }

}

function addCircles() {
    for (var indexY=0 ;indexY<9;indexY++){
        for (var indexX = 0 ;indexX<9;indexX++){
            var c = new Circle();
            gameview.addChild(c);
            circleArr[indexX][indexY]=c;
            c.indexX=indexX;
            c.indexY=indexY;
            c.x=indexY%2?indexX*55+35:indexX*55;
            c.y=indexY*55;

            if(indexX==4 && indexY==4){
                c.setCircleType(3);
                currentCat=c;
            }
            c.addEventListener("click",circleClick)
        }
    }
}
addCircles();