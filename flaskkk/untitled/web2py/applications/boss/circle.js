/**
 * Created by feng.qian on 2016/5/12.
 */
function Circle() {
    createjs.Shape.call(this);
    this.setCircleType = function (type) {
        this._circletype=type;
        switch (type){
            case Circle.TYPE_UNSELECT:
                this.setColor("#cccccc");
                break;
            case Circle.TYPE_SELECT:
                this.setColor("#ff6600");
                break;
            case Circle.TYPE_CAT:
                this.setColor("pink");
                break;
        }
        
    };
    

    this.setColor = function (colorString) {
        this.graphics.beginFill(colorString);
        this.graphics.drawCircle(0,0,25);
        this.graphics.endFill();

    };
    this.getCircleType = function () {
        return this._circletype;
        
    };
    this.setCircleType(1);
}
Circle.prototype = new createjs.Shape();
Circle.TYPE_UNSELECT=1;
Circle.TYPE_SELECT=2;
Circle.TYPE_CAT=3;