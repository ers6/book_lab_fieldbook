
## Reflection
We entered the rare books and manuscript’s library’s reading room as a class for the second time. The books you and Cait selected for our viewing enjoyment varied across genre, but they all featured rich non-textual elements. Many of these included illustrations as they are typically conceived. Others included data visualizations, DIY-navigational instruments, and pop-up visualizations of the earth’s geology. The books that peaked my interest did so for their lack image and overwhelming amount of white space. The majority of Edward Lear’s _Illustrations_ and al de Humboldt’s _Atlas Geographique_ were composed of white space, or paper left unmarked by ink. For this lab, I’m curious what page-as-image analysis affords these illustrator’s use of white space and what that may mean for how digital humanists render, analyze, or neglect it.

Firstly, I describe these page-images and how whitespace functions in both volumes.

Lear’s _Illustrations of the family of Psittacidae, or parrots_
 - Parrot illustrations are supposed to be life sized. The color is
   extremely rich. It looks more like a painting than a book.
 - The pages have to be one sided. There are pieces of tissue paper
   between each blank page and image.
 - only the birds are done in color. Everything else is black and white
   which creates a visual hierarchy of the page. There’s no background
   really. The rest of the image (aside from the birds) looks like a
   sketch that the artist forgot to paint. The only text on the page is
   the bird’s scientific and colloquial names.
 - Amount of white space in the book is striking. Because the artist was
   trying to give the reader a sense of the size of these birds, the
   amount of whitespace left on a page image can be used to compare the
   size of one bird to another. Whitespace isn’t blank space here at
   all- it’s a rhetorical device communicating scale.

al de Humboldt’s _Atlas Geographique._

 - the first thing that caught my eye about the maps was the grayish
   brown splatters on the pages surrounding them.
 - Then I noticed the outline of where the lithography press pushed the
   stone plate into the page. I could feel the impression where it bit
   into the page.
 - The amount of white space surrounding the maps varied as did the
   orientation of the images. Much like Lear’s parrot illustrations,
   Humboldt uses whitespace to communicate the scale of the seized
   territory he is mapping. Some maps will only take up about half the
   area of one page while others extend across the spine and occupy two
   pages.

In both books, the illustrators use white space to communicate scale and, with it, a sense of neutrality (i.e., scale remains consistent across the book to make these images seem factual to the objects they depict even though they are merely remediations of them). Whitespace, while being used to communicate neutrality, is rich with meaning. Additionally, the amount of whitespace in both books is indicative of the lithography process through which both texts were created. All printing is single-sided because a lithography press cannot print images on two sides of a page without destroying the reverse image. The history of the books’ material production is quite literally pressed into the whitespace. While left unmarked by ink, they are certainly marked by human labor. Whitespace across both volumes is anything but blank.

## Towards a Digitization Protocol that Accounts for Whitespace

One of the most successful projects I’ve seen that accounts for whitespace is Melanie Micir and Anna Preuss’s digitization of Hope Mirrlees’ _Paris_ ([https://ada.artsci.wustl.edu/paris/content/paris_current.xml](https://ada.artsci.wustl.edu/paris/content/paris_current.xml))_. Paris_ is a 400 line, modernist poem that Virginia Woolf typeset and printed at her Hogarth Press. In the poem, Mirrlees makes use of strange spacing, and Woolf’s amateurish typesetting also creates odd spaces between lines and words. Rather than normalize these, Micir and Preuss opt to measure the space between each word, line, stanza, and page-margin. They encode this spatial information into their xml edition of the poem. Micir and Preuss’s digital edition is, therefore, specific to the copy of the poem they digitized. It preserves the material realities of typesetting at Hogarth that produced the variant spacing in _Paris._ But Micir and Preuss’s methodologies cannot be replicated at scale. To create an automated protocol for digitization that preserve whitespace, we must look elsewhere towards OCR and DIA.

Whitespace is rarely if ever preserved in text-centric digitization approaches. OCR, for example, famously transforms an image of a page into a “bag of words.” Take Google’s Tesseract for an example. Tesseract transforms an image of page into a black and white version where all marks considered “meaningful” are rendered in black and those considered part of the background (not meaningful) are blotted out in uniform white. This process is called binarization. The goal of this step in Tesseract is to separate intentionally made marks from those made unintentionally. In doing so, it enacts a hierarchy of meaning where marks made with ink are meaningful and those made through some other medium are meaningless. Or, that marks made intentionally are meaningful while unintentional marks are meaningless.

After tesseract transforms an image of a page into this black and white intermediary, it scans for machine readable characters. It transcribes the characters it finds into plain text. In terms of spacing, it preserves spaces between words, line breaks, and paragraph spaces. Tesseract does not encode whitespace on the rest of the page into the plain text remediation. If I were to run Tesseract on images of Lear’s and Humboldt’s volumes, I would likely end up with gibberish. It would almost certainly miss the cursive text on Humboldt’s maps, and it may try to transform the images into textual characters. The amount of whitespace on the pages would not be preserved.

The DIA protocols Piper, Wellmon, and Cheriet describe in their article would be more amenable to a digitization that accounts for white space; however, like OCR, it relies on binarizing images. According to the authors:

> one of the most essential steps in the [DIA] process is that of
> binarization, which is used to differentiate what DIA researchers call
> the foreground and background of a page image (Fig. 1). Qualities that
> are relevant to the process of binarization can include the
> discontinuous color of the page through weathering or
> the bleeding of ink either through the page or across to an adjacent
> page (Piper, Wellmon, and Chertier 271). 

DIA, like OCR, renders the marks its algorithm deemed intentional in black and everything else in uniform white. This would remove the traces of the lithography process left on the Humboldt page images thereby occluding human labor. Likewise, Lear’s color illustrations may be rendered in black and white which would not preserve them well at all. DIA could, however, calculate the amount of a page that is so called background or whitespace. This could be quite useful for studying the use of whitespace at scale. I can imagine this might be helpful in studying how the use of whitespace to communicate scale was politicized in imperial maps, like that of Humboldt. Or, in studying anatomically-to-scale illustrations similar to Lear’s.

Digitization always already enacts a hierarchy of meaning upon the object being digitized. Organizing digitization around page-images destabilizes the text-centric approach that has long dominated digital humanities. It also provides a way to study non-textual elements of page-images at scale. However, it, too, reaches its limits in studying whitespace. These elements, though unmarked with ink, are marked with the human labor that constructs, the technologies that produce, and the storage conditions that preserve/degrade page images. Un-inked space on a page is never blank. DH methods need to be reimagined to account for.
