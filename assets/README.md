# Long Horizon — profile media

An original personal manifesto: a steady identity, four enduring principles, a slow horizon
and sparse points of light. It is independent of any particular project, product or field.

> Think from first principles.
> Build with conviction.
> Stay useful.
> Play the long game.

## Animation and layout

- Desktop SVGs: 1440 × 760. Mobile SVGs: 720 × 940, selected below 768 px viewport width.
- Eight-second CSS animation loop inside a scriptless SVG image. The horizon drifts slightly,
  the glow breathes, points change emphasis, and a bronze emphasis passes across complete
  philosophy lines. The name and all four principles remain visible throughout.
- Separate ink and warm-ivory palettes. SVGs use local system sans/serif font stacks.
- The PNG equivalents are deliberate still compositions, with the final principle accented.
  The README selects them for reduced motion; the SVG also disables animation under the
  same preference. All philosophy text is included in the image's accessible description.
- No scripts, external fonts, tracking, React, canvas runtime or third-party assets.

Generate all eight assets with Python 3 and Playwright/Chromium:

```sh
python scripts/render_hero.py
```

## Design research

Three compositions were compared before publication: Long Horizon (editorial horizon),
Inner Orbit (values surrounding a central identity), and First Form (geometric construction).
Only Long Horizon is published. Rejected prototype images were discarded.

Conceptual research on 21st.dev:

- [CosmicAurora](https://21st.dev/@dhileepkumargm/components/cosmic-aurora): slow light and sparse organic motion, reduced here to a restrained horizon and a few points.
- [Spotlight](https://21st.dev/@manuarora700/components/spotlight): light used to establish hierarchy, translated into an ambient, non-interactive gradient.
- [Text Reveal](https://21st.dev/@dillionverma/components/text-reveal): gradual changes in text emphasis, adapted so every principle stays readable without scroll or typing.

All artwork and animation are newly authored. No component code is copied.
