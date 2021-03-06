/* Sizing and scales. */
var w = 400,
    h = 400,
    x = pv.Scale.linear(0, 99).range(0, w),
    y = pv.Scale.linear(0, 1).range(0, h),
    c = pv.Scale.log(1, 100).range("orange", "brown");

/* The root panel. */
var vis = new pv.Panel()
    .width(w)
    .height(h)
    .bottom(20)
    .left(20)
    .right(10)
    .top(5);

/* Y-axis and ticks. */
vis.add(pv.Rule)
    .data(y.ticks())
    .bottom(y)
    .strokeStyle(function(d) d ? "#eee" : "#000")
  .anchor("left").add(pv.Label)
    .visible(function(d) d > 0 && d < 1)
    .text(y.tickFormat);

/* X-axis and ticks. */
vis.add(pv.Rule)
    .data(x.ticks())
    .left(x)
    .strokeStyle(function(d) d ? "#eee" : "#000")
  .anchor("bottom").add(pv.Label)
    .visible(function(d) d > 0 && d < 100)
    .text(x.tickFormat);

/* The dot plot! */
vis.add(pv.Panel)
    .data(data)
  .add(pv.Dot)
    .left(function(d) x(d.x))
    .bottom(function(d) y(d.y))
    .strokeStyle(function(d) c(d.z))
    .fillStyle(function() this.strokeStyle().alpha(.2))
    .size(function(d) d.z)
    .title(function(d) d.z.toFixed(1));

vis.render();