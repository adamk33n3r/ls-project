# [Insert Title Here]
By Adam Keenan and Dallas Mullet

## Define the domain
Slideshow in the browser
Reveal.js

## Define the problem
Reveal setup and configuration is verbose and tedious. This language is intended
to simplify the slide generation process to make it a better experience.

## Examples

###### simple.config
    ###################
    # '#' means comment.
    # '%' means command.
    # Indentation does not mean anything.
    # Parameters to commands are space delimited.
    # Properties of commands are each on new lines.
    # The properties values are preceded by a colon.
    ###################

    # Configuration
    %config
      controls: true
    %end

    # Formatting
    %format simple
      bg: red
      font-size: 12pt
    %end
    
    # Single Slide
    %slide
      title: Title
      body: Body of text to be displayed
      format: simple
    %end

    # Vertical
    %section
      format: simple
      %slide
        title: Title2
      %end
      %slide
        title: Title3
      %end
    %end 
    
    # Nested vertical
    %section
      format: simple
      %slide
          title: Title4
      %end
      %section
        %slide
          title: Title5
        %end
        %slide
          title: Title6
        %end
      %end
    %end 

###### simple.html

    <script>Reveal.initialize({controls:true});</script>
    <style type="text/css">
        font-size: 12pt;
    </style>
    <div class="reveal">
        <div class="slides">
            <section class="simple" data-background="red">
                <title>Title</title>
                <content>Yay</content>
            </section>
            <section class="simple" data-background="red">
                <section>
                    <title>Title2</title>
                </section>
                <section>
                    <title>Title3</title>
                </section>
            </section>
            <section class="simple" data-background="red">
                <section>
                    <title>Title4</title>
                </section>
                <section>
                    <section>
                        <title>Title5</title>
                    </section>
                    <section>
                        <title>Title6</title>
                    </section>
                </section>
            </section>
        </div>
    </div>
