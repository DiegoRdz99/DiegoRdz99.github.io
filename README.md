# DiegoRdz99.github.io
Cantoral Cristeros

# TXT files
These files contain the songs in a format similar to ProChords, but with some changes.

## Song metadata
The `.txt` file begins with the metadata of the song. The elements are included in a dictionary-like fashion, i.e. `title : Entraré` indicates the title of the song is "Entraré". The possible entries for metadata are (as of now): title, subtitle, composer, key and liturgy.

## Parts
Parts are signaled between slashes, e.g. `/verse/` indicates a verse part, and are placed at the beginning of the part. Part-IDs can be assigned to identify each, e.g. Chorus 1 or Verse 3, after a hyphen. For example, for Chorus 1 we write `/Coro-1/`.

## Chords
Chords are written between brackets, e.g. `[Am]`, and will be placed just above the text right next to it. For example in `Es[C]toy a la [G]puerta y [F]llamo`, the chord C is placed above the 'toy' syllable. One can write any possible chord, with no limitations, as long as no special characters are used. Flats are indicated by "b" and sharps by "#". To indicate major extended chords it's encouraged to use "^" (which renders as Δ) rather than "M". To indicate slash chords like D/F#, inversion notation is used. The chord is written normally but instead of a slash "/" an underscore "_" must be written, and right next to it the interval desired. For example, with D/F# we write `D_3`, since F# is a major third interval of D. If we instead wished D/C, we would write `D_m7`, since C is a minor seventh interval of D. If we wanted D/Ab we write `D_m5`, although strictly speaking it would be a d5 interval, here the "m" simply indicates that the original interval is reduced by one.

## Multiline
To make a line have two voices, the line must start with `{`

## 
