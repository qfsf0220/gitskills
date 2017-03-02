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
var move_none=-1,move_left=0,move_up_left=1,move_up_right=2,move_right=3,move_down_right=4,move_down_left=5;
function getMoveDir(cat) {

    var distenceMap=[];
         //left
        var can = true;
        for (var x = cat.indexX;x>0;x--){
            if (circleArr[x][cat.indexY].getCircleType()==Circle.TYPE_SELECT){
                can = false;
                distenceMap[move_left]=cat.indexX-x;
                break;
            }
        }
    if(can){
        return move_left;
    }
    //left up
    can =true;
    var x = cat.indexX, y =cat.indexY;
    while (true){
        if (circleArr[x][y].getCircleType()==Circle.TYPE_SELECT){
            can = false;
            distenceMap[move_up_left]=cat.indexY-y;
            break;
        }
        if(y%2==0){
            x--;
        }
        y--;
        if(y<0||x<0){
            break;
        }
    }
    if (can){
        return move_up_left;
    }
    //right up
    can = true;
    x = cat.indexX, y = cat.indexY;
    while(true) {
        if (circleArr[x][y].getCircleType() == Circle.TYPE_SELECT) {
            can = false;
            distenceMap[move_up_right] = cat.indexY - y;
            break;
        }

        if(y%2==1){
            x++;
        }
        y--;
        if(y<0||x>8){
            break;
        }
    }

    if(can){
        return move_up_right;
    }

    //right
    can = true ;
    for (var x =cat.indexX;x<9;x++){
        if(circleArr[x][cat.indexY].getCircleType()==Circle.TYPE_SELECT){
            can = false;
            distenceMap[move_right]= x-cat.indexX;
            break;
        }
    }
    if (can){
        return move_right;
    }
    //right down
    can = true;
    x= cat.indexX,y=cat.indexY;
    while (true){
        if (circleArr[x][y].getCircleType()==Circle.TYPE_SELECT){
            can = false;
            distenceMap[move_down_right]=y-cat.indexY;
            break; //?
        }
        if (y%2==1){
            x++;
        }
        y++;
        if(y>8||x>8){
            break;
        }
    }
    if (can){
        return move_down_right
    }
    //left down
    can = true;
    x=cat.indexX , y=cat.indexY;
    while (true){
        if (circleArr[x][y].getCircleType()==Circle.TYPE_SELECT){
            can = false;
            distenceMap[move_down_left]=y-cat.indexY;
            break;
        }
        if(y%2==0){
            x--;
        }
        y++;
        if(y>8||x<0){
            break;
        }
    }
    if (can){
        return move_down_left;
    }

    var maxDir = -1 ,maxValue=-1;
    for (var dir = 0 ;dir <distenceMap.length;dir++){
        if(distenceMap[dir]>maxValue){
            maxValue= distenceMap[dir];
            maxDir=dir;
        }
    }
    if (maxValue>1){
        return maxDir;
    }else {
        return move_none;
    }
}

function circleClick(event) {
    if (event.target.getCircleType() != Circle.TYPE_CAT) {
        event.target.setCircleType(Circle.TYPE_SELECT);
    }else{
        return;
    }

    if (currentCat.indexX==0 ||currentCat.indexX==8 ||currentCat.indexY==0 ||currentCat.indexY==8){
        alert("game over");
        return;
    }


    var dir = getMoveDir(currentCat);
    switch (dir){
        case move_left:
            currentCat.setCircleType(Circle.TYPE_UNSELECT);
            currentCat=circleArr[currentCat.indexX-1][currentCat.indexY];
            currentCat.setCircleType(Circle.TYPE_CAT);
            break;
        case move_up_left:
            currentCat.setCircleType(Circle.TYPE_UNSELECT);
            currentCat=circleArr[currentCat.indexY%2?currentCat.indexX:currentCat.indexX-1][currentCat.indexY-1];
            currentCat.setCircleType(Circle.TYPE_CAT);
            break;
        case move_up_right:
            currentCat.setCircleType(Circle.TYPE_UNSELECT);
            currentCat=circleArr[currentCat.indexY%2?currentCat.indexX+1:currentCat.indexX][currentCat.indexY-1];
            currentCat.setCircleType(Circle.TYPE_CAT);
        case move_right:
            currentCat.setCircleType(Circle.TYPE_UNSELECT);
            currentCat=circleArr[currentCat.indexX+1][currentCat.indexY];
            currentCat.setCircleType(Circle.TYPE_CAT);
            break;
        case move_down_right:
            currentCat.setCircleType(Circle.TYPE_UNSELECT);
            currentCat=circleArr[currentCat.indexY%2?currentCat.indexX+1:currentCat.indexX][currentCat.indexY+1];
            currentCat.setCircleType(Circle.TYPE_CAT);
            break;
        case move_down_left:
            currentCat.setCircleType(Circle.TYPE_UNSELECT);
            currentCat=circleArr[currentCat.indexY%2?currentCat.indexX-1:currentCat.indexX][currentCat.indexY+1];
            currentCat.setCircleType(Circle.TYPE_CAT);
            break;
        default:
            alert("you  win!!")
    }
    
    
}


    // var leftCircle = circleArr[ currentCat.indexX -1 ][ currentCat.indexY ];
    // var rightCircle = circleArr[currentCat.indexX +1 ][currentCat.indexY];
    // var lefttopCircle = circleArr[currentCat.indexX -1 ][currentCat.indexY-1];
    // var righttopCircle = circleArr[currentCat.indexX  ][currentCat.indexY -1];
    // var leftbottomCircle = circleArr[currentCat.indexX -1 ][currentCat.indexY+1];
    // var rightbottomCircle = circleArr[currentCat.indexX  ][currentCat.indexY +1];
    // if (leftCircle.getCircleType()==1){
    //     leftCircle.setCircleType(3);
    //     currentCat.setCircleType(1);
    //     currentCat = leftCircle;
    // }else
    //
    //    if (rightCircle.getCircleType()==1){
    //     rightCircle.setCircleType(3);
    //     currentCat.setCircleType(1);
    //     currentCat = rightCircle;
    // }else
    //      if (lefttopCircle.getCircleType()==1){
    //     lefttopCircle.setCircleType(3);
    //     currentCat.setCircleType(1);
    //     currentCat = lefttopCircle;
    // }else
    //      if (righttopCircle.getCircleType()==1){
    //     righttopCircle.setCircleType(3);
    //     currentCat.setCircleType(1);
    //     currentCat = righttopCircle;
    // }else
    //      if (leftbottomCircle.getCircleType()==1){
    //     leftbottomCircle.setCircleType(3);
    //     currentCat.setCircleType(1);
    //     currentCat = leftbottomCircle;
    // }else
    //      if (rightbottomCircle.getCircleType()==1){
    //     rightbottomCircle.setCircleType(3);
    //     currentCat.setCircleType(1);
    //     currentCat = rightbottomCircle;
    // }else{
    //          alert("you win");
    //      }


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
            }else if (Math.random()<0.1){
                c.setCircleType(Circle.TYPE_SELECT);
            }


            c.addEventListener("click",circleClick)
        }
    }
}
addCircles();