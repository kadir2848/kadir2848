# Profile media

Original locally generated artwork. No tracking, remote font or image-generation service.

- `hero-dark.gif` / `hero-light.gif`: a six-second illustrative event-routing loop.
- `hero-dark.png` / `hero-light.png`: static equivalents selected for reduced motion.
- The README uses standard HTML `picture`, `source` and `img` elements. No JavaScript runs.

Generate with Pillow and a Unicode TrueType font:

```sh
python scripts/render_hero.py --font FONT.ttf
```

The full name and positioning are visible from the first frame. Only the event indicator
moves; the artwork does not imply live activity, throughput or a measured outcome.

Conceptual inspiration: [Animated Grid Pattern](https://21st.dev/@dillionverma/components/animated-grid-pattern)
and [21st.dev's terminal guide](https://21st.dev/blog/terminal-ui-components). No third-party
component source or art is included.
