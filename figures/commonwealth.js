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
    var R = { cx: 410, cy: 110 }, A = { cx: 628, cy: 392 }, T = { cx: 192, cy: 392 };

    // arrows first (so node boxes sit on top of the arrow tails)
    arrow(out, 486, 138, 590, 356, C.slate, 2.4);      // recipients -> asset holders
    txt(out, 600, 250, "lf-tick", C.ink2, "start", str(spec.sell, "sell tokens"));
    arrow(out, 512, 400, 300, 400, C.slate, 2.4);      // asset holders -> treasury
    txt(out, 406, 430, "lf-tick", C.ink2, "middle", str(spec.levy, "pay levy in tokens"));
    arrow(out, 224, 356, 342, 138, C.slate, 2.4);      // treasury -> recipients
    txt(out, 214, 250, "lf-tick", C.ink2, "end", str(spec.dividend, "pay dividend in tokens"));

    // three nodes
    rrect(out, 300, 82, 220, 56, C.boxfill, C.boxln, 1.5, 12);
    txt(out, R.cx, 115, "lf-axis", C.ink, "middle", str(nodes.recipients, "Dividend recipients"));
    rrect(out, 520, 364, 216, 56, C.boxfill, C.boxln, 1.5, 12);
    txt(out, A.cx, 397, "lf-axis", C.ink, "middle", str(nodes.holders, "Asset holders"));
    rrect(out, 84, 364, 216, 56, C.boxfill, C.boxln, 1.5, 12);
    txt(out, T.cx, 397, "lf-axis", C.ink, "middle", str(nodes.treasury, "Treasury"));

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

  var TYPES = [
    ["commonwealth-stack", buildStack],
    ["commonwealth-loop",  buildLoop],
    ["commonwealth-rings", buildRings]
  ];
  for (var i = 0; i < TYPES.length; i++) {
    DossierFigures.registerPoster(TYPES[i][0], posterFrom(TYPES[i][1]));   // sealer dispatches by spec.type
    DossierFigures.registerRenderer(TYPES[i][0], liveFrom(TYPES[i][1]));   // lightbox dispatches by spec.type
  }
})(typeof window !== "undefined" ? window : null);
