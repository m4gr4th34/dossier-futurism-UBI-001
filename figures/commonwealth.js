/*
 * commonwealth.js — three static schematic render modules for the Commonwealth
 * Protocol conjecture (Dossier Futurism-UBI-001, Part II). Domain: mechanism design.
 *
 * WHAT THIS IS
 *   Vendored, zero-dependency, reader-side render modules for three NON-interactive
 *   explanatory diagrams — a layer stack, a circular demand loop, and concentric
 *   entry rings. Each carries a finding, not a data plot, so it uses NONE of the
 *   astronomy primitives (PRNG / zoom / scatter / time); it only composes
 *   el() / escAttr / escTxt / r2 from the runtime, per the composition law. Loaded
 *   after figures.js; extends window.DossierFigures with three render fns + posters.
 *
 * SHARED-COMPUTE SPLIT (floor == ceiling by construction)
 *   Each build*(spec) computes the WHOLE scene once as a flat list of primitive
 *   shape descriptors { tag, attrs, text? }. The live path turns each into an el()
 *   DOM node; the poster path serializes each into an SVG string. Neither path owns
 *   geometry, so the JS-off floor can never drift from the live ceiling.
 *
 * TYPES (declared as spec.type in the figure's data-figure):
 *   "commonwealth-stack" — four-layer stack with a constitutional firewall
 *   "commonwealth-loop"  — three-node chartalist demand loop
 *   "commonwealth-rings" — three concentric entry rings
 *   All text is content, carried in the spec; the module only lays it out. Text is
 *   sized via tier CLASSES only (lf-callout / lf-axis / lf-tick), never a raw
 *   font-size — the runtime owns the size (see figures/README.md).
 */
(function (root) {
  "use strict";

  var NS = root && root.DossierFigures;
  if (!NS) {
    if (root && root.console) {
      root.console.error("[commonwealth] figures.js runtime not found — load figures.js before commonwealth.js");
    }
    return;
  }

  // COMPOSITION: every primitive below IS the runtime's — never re-rolled.
  var DossierFigures = NS;
  var el      = DossierFigures.el;
  var escAttr = DossierFigures.escAttr;
  var escTxt  = DossierFigures.escTxt;
  var r2      = DossierFigures.r2;

  // Palette — dark ink on a light self-painted stage, so the schematic reads on any
  // host card (light or dark) without depending on host CSS.
  var C = {
    bg:      "#f3f6f5",
    ink:     "#17262c",
    ink2:    "#5f7075",
    teal:    "#0c8f86",
    slate:   "#4b5a61",
    boxln:   "#9ab5ad",
    boxfill: "#ffffff",
    wall:    "#17262c",
    r1:      "#cfe0db",
    r2c:     "#dfeae7",
    r3:      "#eef3f2",
    levy:    "#b06a1f",
    div:     "#0c8f86"
  };

  function num(v, d) { return (typeof v === "number" && isFinite(v)) ? v : d; }
  function arr(v) { return Object.prototype.toString.call(v) === "[object Array]" ? v : []; }
  function str(v, d) { return (typeof v === "string" && v) ? v : d; }

  // ---- primitive pushers (all coordinates rounded via r2) --------------------
  function rrect(out, x, y, w, h, fill, stroke, sw, rx) {
    out.push({ tag: "rect", attrs: {
      x: r2(x), y: r2(y), width: r2(w), height: r2(h), rx: (rx == null ? 12 : rx),
      fill: fill, stroke: stroke, "stroke-width": sw } });
  }
  function line(out, x1, y1, x2, y2, stroke, sw, dash) {
    var a = { x1: r2(x1), y1: r2(y1), x2: r2(x2), y2: r2(y2), stroke: stroke, "stroke-width": sw, "stroke-linecap": "round" };
    if (dash) a["stroke-dasharray"] = dash;
    out.push({ tag: "line", attrs: a });
  }
  function circle(out, cx, cy, r, fill, stroke, sw) {
    out.push({ tag: "circle", attrs: { cx: r2(cx), cy: r2(cy), r: r2(r), fill: fill, stroke: stroke, "stroke-width": sw } });
  }
  function txt(out, x, y, cls, fill, anchor, s, transform) {
    var a = { x: r2(x), y: r2(y), "class": cls, fill: fill, "text-anchor": anchor };
    if (transform) a.transform = transform;
    out.push({ tag: "text", attrs: a, text: s });
  }
  function tlines(out, x, y, dy, cls, fill, anchor, lines) {
    for (var i = 0; i < lines.length; i++) txt(out, x, y + i * dy, cls, fill, anchor, lines[i]);
  }
  // arrow = line + a filled triangular head at (x2,y2), oriented along the segment.
  function arrow(out, x1, y1, x2, y2, color, sw) {
    line(out, x1, y1, x2, y2, color, sw);
    var ang = Math.atan2(y2 - y1, x2 - x1), s = 10, wdt = 0.5;
    var ca = Math.cos(ang), sa = Math.sin(ang);
    var bx = x2 - s * ca, by = y2 - s * sa;
    var p = r2(x2) + "," + r2(y2) + " " +
            r2(bx + s * wdt * sa) + "," + r2(by - s * wdt * ca) + " " +
            r2(bx - s * wdt * sa) + "," + r2(by + s * wdt * ca);
    out.push({ tag: "polygon", attrs: { points: p, fill: color } });
  }
  // a titled panel: rounded box + centered name + centered sub-lines.
  function panel(out, x, y, w, h, name, lines) {
    rrect(out, x, y, w, h, C.boxfill, C.boxln, 1.5, 12);
    var cx = x + w / 2;
    txt(out, cx, y + 26, "lf-axis", C.ink, "middle", name);
    tlines(out, cx, y + 50, 20, "lf-tick", C.ink2, "middle", arr(lines));
  }

  // The demand-loop triangle vertices: R (recipients, top), A (asset holders, bottom-right),
  // T (treasury, bottom-left). SHARED COMPUTE — buildLoop draws the full figure from these, and
  // the commonwealth-engine mini-loop reuses the SAME function at a small scale, so the loop
  // geometry is never duplicated. Called with buildLoop's own coords it reproduces them exactly.
  function loopPoints(cx, cyTop, cyBot, halfW) {
    return { R: { x: cx, y: cyTop }, A: { x: cx + halfW, y: cyBot }, T: { x: cx - halfW, y: cyBot } };
  }

  // ---- FIGURE 1: the layer stack + constitutional firewall -------------------
  function buildStack(spec) {
    var W = 820, H = 540, out = [];
    out.push({ tag: "rect", attrs: { x: 0, y: 0, width: W, height: H, fill: str(spec.stage, C.bg) } });

    var fw = spec.firewall || {};
    var reg = spec.registry || {};
    var stack = arr(spec.stack);

    // firewall: a bold vertical line separating Layer 0 from the money stack
    line(out, 298, 70, 298, 490, C.wall, 3, "2 6");
    txt(out, 286, 175, "lf-axis", C.wall, "middle", str(fw.label, "constitutional firewall"), "rotate(-90 286 175)");
    txt(out, 270, 175, "lf-tick", C.ink2, "middle", str(fw.sub, "no shared governance · no treasury exposure"), "rotate(-90 270 175)");

    // Layer 0 — registry (left of the firewall), aligned with Layer 1
    panel(out, 40, 360, 232, 126, str(reg.name, "LAYER 0 · Personhood registry"), reg.lines);

    // money stack (right of the firewall): Layer 3 top -> Layer 1 bottom
    var boxes = [ { y: 70, h: 118 }, { y: 204, h: 138 }, { y: 372, h: 114 } ];
    for (var i = 0; i < 3 && i < stack.length; i++) {
      panel(out, 330, boxes[i].y, 452, boxes[i].h, str(stack[i].name, ""), stack[i].lines);
    }

    // levy flows Layer 2 -> Layer 1 (down, inside the stack)
    arrow(out, 556, 344, 556, 370, C.levy, 2.4);
    txt(out, 580, 361, "lf-tick", C.levy, "start", str(spec.levyLabel, "levy"));

    // dividend crosses the firewall Layer 1 -> Layer 0 (the ONE permitted crossing)
    arrow(out, 330, 423, 274, 423, C.div, 2.4);
    txt(out, 302, 414, "lf-tick", C.div, "middle", str(spec.dividendLabel, "dividend"));

    return { W: W, H: H, ariaLabel: str(spec.title, "The Commonwealth Protocol layer stack"), nodes: out };
  }

  // ---- FIGURE 2: the chartalist demand loop (three nodes) --------------------
  function buildLoop(spec) {
    var W = 820, H = 520, out = [];
    out.push({ tag: "rect", attrs: { x: 0, y: 0, width: W, height: H, fill: str(spec.stage, C.bg) } });

    var nodes = spec.nodes || {};
    var LP = loopPoints(410, 110, 392, 218), R = LP.R, A = LP.A, T = LP.T;

    // arrows first (so node boxes sit on top of the arrow tails)
    arrow(out, 486, 138, 590, 356, C.slate, 2.4);      // recipients -> asset holders
    txt(out, 600, 250, "lf-tick", C.ink2, "start", str(spec.sell, "sell tokens"));
    arrow(out, 512, 400, 300, 400, C.slate, 2.4);      // asset holders -> treasury
    txt(out, 406, 430, "lf-tick", C.ink2, "middle", str(spec.levy, "pay levy in tokens"));
    arrow(out, 224, 356, 342, 138, C.slate, 2.4);      // treasury -> recipients
    txt(out, 214, 250, "lf-tick", C.ink2, "end", str(spec.dividend, "pay dividend in tokens"));

    // three nodes
    rrect(out, 300, 82, 220, 56, C.boxfill, C.boxln, 1.5, 12);
    txt(out, R.x, 115, "lf-axis", C.ink, "middle", str(nodes.recipients, "Dividend recipients"));
    rrect(out, 520, 364, 216, 56, C.boxfill, C.boxln, 1.5, 12);
    txt(out, A.x, 397, "lf-axis", C.ink, "middle", str(nodes.holders, "Asset holders"));
    rrect(out, 84, 364, 216, 56, C.boxfill, C.boxln, 1.5, 12);
    txt(out, T.x, 397, "lf-axis", C.ink, "middle", str(nodes.treasury, "Treasury"));

    // center annotation: the floor identity
    txt(out, 410, 250, "lf-callout", C.teal, "middle", str(spec.floor, "floor value ≈ τ·W ⁄ v"));
    txt(out, 410, 274, "lf-tick", C.ink2, "middle", str(spec.floorSub, "levy rate × wrapped base ÷ velocity"));

    // side note
    txt(out, 806, 34, "lf-tick", C.ink2, "end", str(spec.note, "the sink every failed crypto-UBI lacked"));

    return { W: W, H: H, ariaLabel: str(spec.title, "The chartalist demand loop"), nodes: out };
  }

  // ---- FIGURE 3: concentric entry rings --------------------------------------
  function buildRings(spec) {
    var W = 820, H = 580, out = [];
    out.push({ tag: "rect", attrs: { x: 0, y: 0, width: W, height: H, fill: str(spec.stage, C.bg) } });

    var cx = 410, cy = 288, rings = arr(spec.rings);
    // outer -> inner (draw largest first so inner sits on top)
    circle(out, cx, cy, 226, C.r3, C.boxln, 1.5);
    circle(out, cx, cy, 158, C.r2c, C.boxln, 1.5);
    circle(out, cx, cy, 92, C.r1, C.boxln, 1.5);

    // label blocks stacked in the upper half, each inside its own band
    var r3 = rings[2] || {}, r2r = rings[1] || {}, r1 = rings[0] || {};
    txt(out, cx, 80, "lf-axis", C.ink, "middle", str(r3.name, "RING 3 · real property"));
    tlines(out, cx, 100, 18, "lf-tick", C.ink2, "middle", arr(r3.lines));
    txt(out, cx, 152, "lf-axis", C.ink, "middle", str(r2r.name, "RING 2 · tokenized financial"));
    tlines(out, cx, 172, 18, "lf-tick", C.ink2, "middle", arr(r2r.lines));
    txt(out, cx, 262, "lf-axis", C.ink, "middle", str(r1.name, "RING 1 · protocol-native"));
    tlines(out, cx, 282, 18, "lf-tick", C.ink2, "middle", arr(r1.lines));

    // outside annotation, below the rings
    txt(out, cx, 548, "lf-axis", C.slate, "middle", str(spec.note, "on-chain title worked only where the state already worked"));

    return { W: W, H: H, ariaLabel: str(spec.title, "Entry by rings"), nodes: out };
  }

  // ---- FIGURE 4: the viability frontier ("commonwealth-engine") --------------
  // The runtime ships no chart primitives yet (axes / value->pixel scales / plotting; see
  // figures/README.md), so this figure carries its own — composing el()/escAttr via the shared
  // node list, exactly like the schematics. Every NUMBER comes from the data-figure spec, which
  // Code generates from commonwealth_model.json (single source; never hand-typed twice).
  var CH = {
    band1: "#eaf3f0",   // poverty-relevant band
    band2: "#dbeae5",   // floor band
    bandLW: "#f7ece0",  // living-wage band (drawn to show it sits UNREACHED above the curves)
    tau1: "#9ab5ad", tau2: "#0c8f86", tau3: "#17262c",
    dot: "#b06a1f", axis: "#c2cdc9"
  };
  function engineGeom() { return { W: 900, H: 560, L: 108, R: 792, T: 54, B: 462 }; }
  function money(v) {
    if (v >= 1e6) return "$" + (v / 1e6) + "M";
    if (v >= 1000) return "$" + (v / 1000) + "k";
    return "$" + v;
  }
  function makeScales(spec, g) {
    var xmin = num((spec.x || {}).min, 100), xmax = num((spec.x || {}).max, 200000);
    var ymin = num((spec.y || {}).min, 1), ymax = num((spec.y || {}).max, 20000);
    var lx0 = Math.log(xmin), lx1 = Math.log(xmax), ly0 = Math.log(ymin), ly1 = Math.log(ymax);
    return {
      xmin: xmin, xmax: xmax, ymin: ymin, ymax: ymax,
      X: function (w) { return g.L + (g.R - g.L) * (Math.log(w) - lx0) / (lx1 - lx0); },
      Y: function (d) { return g.B - (g.B - g.T) * (Math.log(Math.max(d, ymin)) - ly0) / (ly1 - ly0); }
    };
  }

  function buildEngine(spec) {
    var g = engineGeom(), W = g.W, H = g.H, out = [], sc = makeScales(spec, g);
    var tiers = arr(spec.tiers), scen = arr(spec.scenarios), fTau = arr(spec.frontierTau);
    out.push({ tag: "rect", attrs: { x: 0, y: 0, width: W, height: H, fill: str(spec.stage, C.bg) } });

    // tier bands (regions between thresholds; the living-wage band is drawn to expose it as unreached)
    function band(dlo, dhi, fill) {
      var y1 = sc.Y(dhi), y2 = sc.Y(dlo);
      out.push({ tag: "rect", attrs: { x: g.L, y: r2(y1), width: r2(g.R - g.L), height: r2(y2 - y1), fill: fill } });
    }
    var thr = tiers.map(function (t) { return t.d; });
    if (thr.length >= 3) {
      band(thr[0], thr[1], CH.band1);
      band(thr[1], thr[2], CH.band2);
      band(thr[2], sc.ymax, CH.bandLW);
    }
    // tier threshold lines + LEFT-edge labels (keeps the busy right edge for curve labels)
    for (var i = 0; i < tiers.length; i++) {
      var yy = sc.Y(tiers[i].d);
      line(out, g.L, yy, g.R, yy, C.boxln, 1, "3 5");
      txt(out, g.L + 6, yy - 6, "lf-tick", C.ink2, "start", str(tiers[i].label, money(tiers[i].d)));
    }
    // axes
    line(out, g.L, g.T, g.L, g.B, CH.axis, 1.5);
    line(out, g.L, g.B, g.R, g.B, CH.axis, 1.5);
    var xt = [100, 1000, 10000, 100000, 200000];
    for (var xi = 0; xi < xt.length; xi++) {
      if (xt[xi] < sc.xmin || xt[xi] > sc.xmax) continue;
      var xx = sc.X(xt[xi]);
      line(out, xx, g.B, xx, g.B + 5, CH.axis, 1.2);
      txt(out, xx, g.B + 20, "lf-tick", C.ink2, "middle", money(xt[xi]));
    }
    txt(out, (g.L + g.R) / 2, g.B + 42, "lf-axis", C.ink, "middle", "wrapped wealth per member  (W ⁄ P)");
    var yt = [1, 10, 100, 1000, 10000];
    for (var yi = 0; yi < yt.length; yi++) {
      if (yt[yi] < sc.ymin || yt[yi] > sc.ymax) continue;
      var yv = sc.Y(yt[yi]);
      line(out, g.L - 5, yv, g.L, yv, CH.axis, 1.2);
      txt(out, g.L - 9, yv + 4, "lf-tick", C.ink2, "end", money(yt[yi]));
    }
    txt(out, g.L, g.T - 24, "lf-tick", C.ink2, "start", "dividend $/yr");
    // frontier curves d = tau*W/P (a straight line on log-log; sampled across the x-range)
    var tc = [CH.tau1, CH.tau2, CH.tau3];
    for (var ti = 0; ti < fTau.length; ti++) {
      var tau = fTau[ti], pts = [], N = 24;
      for (var k = 0; k <= N; k++) {
        var w = Math.exp(Math.log(sc.xmin) + (Math.log(sc.xmax) - Math.log(sc.xmin)) * k / N);
        pts.push(r2(sc.X(w)) + "," + r2(sc.Y(tau * w)));
      }
      out.push({ tag: "polyline", attrs: { points: pts.join(" "), fill: "none", stroke: tc[ti % 3], "stroke-width": 2, "stroke-linejoin": "round", "stroke-linecap": "round" } });
      txt(out, sc.X(sc.xmax) - 4, sc.Y(tau * sc.xmax) - 6, "lf-tick", tc[ti % 3], "end", "τ=" + r2(tau * 100) + "%");
    }
    // scenario dots + labels; a right-half dot labels to its LEFT (anchor end) so nothing
    // runs off the plot edge, a left-half dot labels to its right.
    var xmid = (g.L + g.R) / 2;
    for (var si = 0; si < scen.length; si++) {
      var s = scen[si], px = sc.X(s.w), py = sc.Y(s.d), right = px > xmid;
      out.push({ tag: "circle", attrs: { cx: r2(px), cy: r2(py), r: 5, fill: CH.dot, stroke: "#ffffff", "stroke-width": 1.5 } });
      txt(out, px + (right ? -9 : 9), py + (si % 2 ? 15 : -9), "lf-tick", C.ink, right ? "end" : "start", str(s.label, s.name));
    }
    // the honest-ceiling annotation, tucked in the empty band between the floor and
    // living-wage lines on the left (no curve reaches that high at low W/P)
    txt(out, g.L + 28, sc.Y(5200), "lf-tick", CH.dot, "start", str(spec.ceilingNote, ""));
    return { W: W, H: H, ariaLabel: str(spec.title, "The Commonwealth Protocol viability frontier"), nodes: out };
  }

  // ---- generic live + poster emitters from a build fn ------------------------
  function parse(spec) {
    if (typeof spec === "string") { try { return JSON.parse(spec); } catch (e) { return null; } }
    return spec || null;
  }
  function liveFrom(build) {
    return function (container, spec) {
      if (!container) return null;
      if (spec == null && container.getAttribute) spec = container.getAttribute("data-figure");
      spec = parse(spec);
      if (!spec) return null;
      DossierFigures.dedupPoster(container);
      var f = build(spec);
      var svg = el("svg", { viewBox: "0 0 " + f.W + " " + f.H, width: "100%", "class": "lf-svg", role: "img", "aria-label": f.ariaLabel });
      for (var i = 0; i < f.nodes.length; i++) {
        var n = f.nodes[i], node = el(n.tag, n.attrs);
        if (n.text != null) node.textContent = n.text;
        svg.appendChild(node);
      }
      container.appendChild(svg);
      return svg;
    };
  }
  function posterFrom(build) {
    return function (spec) {
      spec = parse(spec);
      if (!spec) return "";
      var f = build(spec);
      var s = '<svg viewBox="0 0 ' + f.W + ' ' + f.H + '" width="100%" class="lf-svg" role="img" aria-label="' + escAttr(f.ariaLabel) + '">';
      for (var i = 0; i < f.nodes.length; i++) {
        var n = f.nodes[i], a = n.attrs, attrStr = "";
        for (var k in a) { if (Object.prototype.hasOwnProperty.call(a, k)) attrStr += " " + k + '="' + escAttr(a[k]) + '"'; }
        s += "<" + n.tag + attrStr + ">" + (n.text != null ? escTxt(n.text) : "") + "</" + n.tag + ">";
      }
      return s + "</svg>";
    };
  }

  // ---- LIVE renderer for commonwealth-engine (lightbox only): the static frontier
  //      PLUS two sliders, scenario chips, a live readout, a moving "you are here" marker,
  //      and an animated demand loop (token dots circulating at rate proportional to tau*W/P,
  //      the same levy flow the model computes). Slider math is the SAME formula as
  //      flow_model.py (d = tau*W/P; first-year net = (1-rho)*tau*W/P), with rho/y read from
  //      the spec constants (sourced from commonwealth_model.json). Browser-only; never run in
  //      Node (the sealer calls posterFrom(buildEngine), not this). -------------------------
  function commas(n) { return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, ","); }
  function mkRange(labelText, min, max, step) {
    var wrap = document.createElement("label"); wrap.className = "lf-field";
    var lab = document.createElement("span"); lab.textContent = labelText;
    var input = document.createElement("input");
    input.type = "range"; input.className = "lf-range";
    input.min = min; input.max = max; input.step = step;
    var val = document.createElement("span"); val.className = "lf-field-val";
    wrap.appendChild(lab); wrap.appendChild(input); wrap.appendChild(val);
    return { wrap: wrap, input: input, val: val };
  }
  function renderEngine(container, spec) {
    if (!container) return null;
    if (spec == null && container.getAttribute) spec = container.getAttribute("data-figure");
    spec = parse(spec);
    if (!spec) return null;
    DossierFigures.dedupPoster(container);

    var g = engineGeom(), sc = makeScales(spec, g);
    var cst = spec.constants || {}, rho = num(cst.rho, 0.2);
    var tiers = arr(spec.tiers), scen = arr(spec.scenarios);

    // static chart (identical geometry to the sealed poster)
    var f = buildEngine(spec);
    var svg = el("svg", { viewBox: "0 0 " + f.W + " " + f.H, width: "100%", "class": "lf-svg", role: "img", "aria-label": f.ariaLabel });
    for (var i = 0; i < f.nodes.length; i++) { var n = f.nodes[i], nd = el(n.tag, n.attrs); if (n.text != null) nd.textContent = n.text; svg.appendChild(nd); }

    // live "you are here" marker
    var halo = el("circle", { cx: -99, cy: -99, r: 12, fill: "none", stroke: "#cf5d36", "stroke-width": 1.5, opacity: 0.5 });
    var mark = el("circle", { cx: -99, cy: -99, r: 7, fill: "#cf5d36", stroke: "#ffffff", "stroke-width": 2 });
    svg.appendChild(halo); svg.appendChild(mark);

    // animated demand loop (reuses loopPoints — no duplicated geometry) in the low-left corner
    var lp = loopPoints(182, 372, 430, 46), order = [lp.R, lp.A, lp.T, lp.R];
    for (var e = 0; e < 3; e++) svg.appendChild(el("line", { x1: order[e].x, y1: order[e].y, x2: order[e + 1].x, y2: order[e + 1].y, stroke: C.boxln, "stroke-width": 1.2, "stroke-linecap": "round" }));
    var loopLab = el("text", { x: 182, y: 448, "class": "lf-tick", fill: C.ink2, "text-anchor": "middle" });
    loopLab.textContent = "the loop, live"; svg.appendChild(loopLab);
    var toks = [];
    for (var t2 = 0; t2 < 3; t2++) { var tk = el("circle", { cx: -9, cy: -9, r: 3.2, fill: C.div }); svg.appendChild(tk); toks.push(tk); }
    function loopPos(p) {
      var pe = ((p % 3) + 3) % 3, ee = Math.floor(pe), fr = pe - ee, a = order[ee], b = order[ee + 1];
      return { x: a.x + (b.x - a.x) * fr, y: a.y + (b.y - a.y) * fr };
    }

    container.appendChild(svg);

    // controls
    var lnmin = Math.log(sc.xmin), lnmax = Math.log(sc.xmax);
    function sliderToW(s) { return Math.exp(lnmin + (lnmax - lnmin) * s / 1000); }
    function wToSlider(w) { return 1000 * (Math.log(w) - lnmin) / (lnmax - lnmin); }
    function tierOf(d) { var nm = "symbolic"; for (var i = 0; i < tiers.length; i++) if (d >= tiers[i].d) nm = str(tiers[i].label, String(tiers[i].d)); return nm; }

    var ctrls = document.createElement("div"); ctrls.className = "lf-controls";
    var tauF = mkRange("levy τ", 0, 5, 0.1), wF = mkRange("wealth / member", 0, 1000, 1);
    var readout = document.createElement("span"); readout.className = "lf-readout";
    var chips = document.createElement("span"); chips.className = "lf-field";
    ctrls.appendChild(tauF.wrap); ctrls.appendChild(wF.wrap); ctrls.appendChild(chips); ctrls.appendChild(readout);
    container.appendChild(ctrls);

    var state = { tau: num(cst.tau_eval, 0.02), w: 50000 };
    function update() {
      var dSus = state.tau * state.w, dFy = (1 - rho) * state.tau * state.w;
      var mx = sc.X(state.w), my = sc.Y(dSus);
      mark.setAttribute("cx", r2(mx)); mark.setAttribute("cy", r2(my));
      halo.setAttribute("cx", r2(mx)); halo.setAttribute("cy", r2(my));
      tauF.val.textContent = r2(state.tau * 100) + "%";
      wF.val.textContent = money(Math.round(state.w));
      readout.textContent = "$" + commas(dSus) + "/yr sustained · $" + commas(dFy) + " first-year · tier: " + tierOf(dSus);
    }
    tauF.input.addEventListener("input", function () { state.tau = parseFloat(tauF.input.value) / 100; update(); });
    wF.input.addEventListener("input", function () { state.w = sliderToW(parseFloat(wF.input.value)); update(); });
    for (var si = 0; si < scen.length; si++) {
      (function (s) {
        var b = document.createElement("button"); b.type = "button"; b.className = "lf-btn"; b.textContent = s.name;
        b.addEventListener("click", function () {
          state.tau = num(cst.tau_eval, 0.02); state.w = s.w;
          tauF.input.value = state.tau * 100; wF.input.value = wToSlider(s.w); update();
        });
        chips.appendChild(b);
      })(scen[si]);
    }
    tauF.input.value = state.tau * 100; wF.input.value = wToSlider(state.w); update();

    // animate the loop; speed proportional to the levy flow tau*W/P. Stops itself once the
    // lightbox closes and detaches the SVG (isConnected guard) — no leaked rAF.
    var p = 0, last = null;
    if (DossierFigures.prefersReducedMotion()) {
      for (var t3 = 0; t3 < toks.length; t3++) { var pp = loopPos(t3); toks[t3].setAttribute("cx", r2(pp.x)); toks[t3].setAttribute("cy", r2(pp.y)); }
    } else {
      var frame = function (ts) {
        if (!svg.isConnected) return;
        if (last == null) last = ts;
        var dt = Math.min((ts - last) / 1000, 0.05); last = ts;
        p += dt * (0.4 + Math.min(state.tau * state.w / 1500, 3.0));
        for (var t = 0; t < toks.length; t++) { var q = loopPos(p + t); toks[t].setAttribute("cx", r2(q.x)); toks[t].setAttribute("cy", r2(q.y)); }
        requestAnimationFrame(frame);
      };
      requestAnimationFrame(frame);
    }
    return svg;
  }

  var TYPES = [
    ["commonwealth-stack", buildStack],
    ["commonwealth-loop",  buildLoop],
    ["commonwealth-rings", buildRings]
  ];
  for (var i = 0; i < TYPES.length; i++) {
    DossierFigures.registerPoster(TYPES[i][0], posterFrom(TYPES[i][1]));   // sealer dispatches by spec.type
    DossierFigures.registerRenderer(TYPES[i][0], liveFrom(TYPES[i][1]));   // lightbox dispatches by spec.type
  }
  // commonwealth-engine: STATIC poster via the shared node list; CUSTOM live renderer (sliders +
  // animated loop) — so it registers renderEngine, not the generic liveFrom.
  DossierFigures.registerPoster("commonwealth-engine", posterFrom(buildEngine));
  DossierFigures.registerRenderer("commonwealth-engine", renderEngine);
})(typeof window !== "undefined" ? window : null);
