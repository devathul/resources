# Programming Resources


## Table of Contents


## General
- Inspiration!: https://www.chessprogramming.org/Keith_Gorlen
- Bit twiddling hacks: http://graphics.stanford.edu/~seander/bithacks.html
- Interesting programming languages: https://www.btbytes.com/pl.html
- Christopher Alexander's Design Patterns: http://www.patternlanguage.com/leveltwo/caframe.htm?/leveltwo/../bios/designpatterns.htm
- https://en.wikipedia.org/wiki/One-instruction_set_computer


## Project Ideas
- script that calls pd noise patch, generates artwork and posts to bandcamp or another file sharing service via selenium
- write some RTS demo sketches 
  - https://sandruski.github.io/RTS-Group-Movement/
  - Nav meshes: https://medium.com/@mscansian/a-with-navigation-meshes-246fd9e72424
  - Boids: http://www.red3d.com/cwr/boids/
- write a time clock web app and keep exact totals for freelance work
- write a stack machine
- stack overflow comments sentiment analyzer
- make an IR-\>spim runner in node/mips compiler + host on heroku
- https://en.wikipedia.org/wiki/Tic-tac-toe_variants
- write an app that scrapes recent posts by favorite SO users
- Challenge/project idea lists:
  - https://www.webfx.com/blog/web-design/10-puzzle-websites-to-sharpen-your-programming-skills/
  - https://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/
- Look for projects at Rosetta Code: http://rosettacode.org/wiki/Rosetta_Code
- "Programming by Doing" simple projects for students: https://programmingbydoing.com/
- Organize mp3s: beets.io and https://www.discogs.com/developers/
- The Logo Foundation: http://el.media.mit.edu/logo-foundation/index.html
- NetLogo: https://en.wikipedia.org/wiki/NetLogo
- write a non-acct twitter (or SO) client that can fav and show imgs like birdfeed without having an account.
- write a sandboxed compiler+code runner
- write a winamp plugin that broadcasts now playing to node API on glitch
  - http://wiki.winamp.com/wiki/Beginner%27s_Basic_Plugin_Guide
  - http://forums.winamp.com/showthread.php?t=224914
- Make a simple DIY label CMS or bandcamp clone; host on Heroku
- Langs/frameworks/libs to learn: COBOL, LISP, Go
- Listening journal or similar using blogger API: https://developers.google.com/blogger/docs/3.0/getting_started 
- make a music player app based on mpg123: https://github.com/TooTallNate/node-lame/blob/master/deps/mpg123/doc/README.remote
  - https://stackoverflow.com/questions/35781991/run-a-command-that-needs-input-without-hanging-but-still-allow-input
  - https://sourceforge.net/p/mpg123/mailman/mpg123-users/thread/CAN5OgQWuYFt4mbbjDZcxMMdTQLZoNiF8AgH5S8Z8rwraN%2B65uA%40mail.gmail.com/
  - https://arstechnica.com/civis/viewtopic.php?f=20&t=850451
- Voice/video chat or stream with WebRTC: https://webrtc.github.io/samples/src/content/capture/canvas-video/  
- Tiger to JS transpiler
- Google Docs but all vim/markdown. Could add multiplayer multicolor text editor/highlighter. Could be a good edutech project.


## Project Euler
- Next to solve: 189, 244
- #93 Sudoku can also be solved using Integer Linear Programming: https://www.coin-or.org/PuLP/CaseStudies/a_sudoku_problem.html
- #84 Monopoly is one of the best. Worth solving using both simulation (I used first-class functions) and stochastic matrix (I used numpy). Working out the initial probabilities for the stochastic matrix requires only basic probability, but it's tricky.
- Euler's totient function: http://www.geeksforgeeks.org/eulers-totient-function/


## Algorithms
- Princeton Algorithms: https://algs4.cs.princeton.edu/home/
- Stanford CS Education Library: http://cslibrary.stanford.edu/
- Berkeley CS61B lectures: https://inst.eecs.berkeley.edu/~cs61b/fa17/materials/lectures/ 
- Yale CPSC 223: http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html
- Algorithm archive: https://www.algorithm-archive.org/
- Skip list: https://en.wikipedia.org/wiki/Skip_list
- Splay tree: https://en.wikipedia.org/wiki/Splay_tree
- Word ladder: https://www.geeksforgeeks.org/word-ladder-length-of-shortest-chain-to-reach-a-target-word/
- Disjoint set/ union find: https://www.hackerearth.com/practice/notes/disjoint-set-union-union-find/
- Segment trees: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/tutorial/
- Self-avoiding walk: https://en.wikipedia.org/wiki/Self-avoiding_walk
- Bellman-Ford: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
- Princeton algorithm assignments: http://www.cs.princeton.edu/courses/archive/spr10/cos226/assignments.html
- Boyer-Moore majority vote algorithm: https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
- Sieve of Eratosthenes: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
- Fermat's factorization method: https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
- Euclid's algorithm: http://andreinc.net/2010/12/11/euclids-algorithm-reducing-fraction-to-lowest-terms/
- Karatsuba algorithm: https://en.wikipedia.org/wiki/Karatsuba_algorithm
- Simplify a fraction: http://codereview.stackexchange.com/questions/66450/simplify-a-fraction
- Basil & Fabian: http://blog.jamisbuck.org/
- Car talk puzzlers: https://developmentality.wordpress.com/tag/car-talk/
- Sliding puzzle solving with hill climbing: https://towardsdatascience.com/solve-slide-puzzle-with-hill-climbing-search-algorithm-d7fb93321325
- Dancing Links: https://www.ocf.berkeley.edu/~jchu/publicportal/sudoku/0011047.pdf

### DP
- Coin change: https://runestone.academy/runestone/books/published/pythonds/Recursion/DynamicProgramming.html
- Maximum subarray problem (Kadane's algorithm): https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm_(Algorithm_3:_Dynamic_Programming)
- Box stacking problem (and other DP problems): https://people.cs.clemson.edu/~bcdean/dp_practice/
- DP text justify: https://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/
- DP coin change: http://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/
- MIT open courseware DP lecture: https://www.youtube.com/watch?v=ocZMDMZwhCY
- Algs/DP: https://people.eecs.berkeley.edu/~vazirani/algorithms/chap6.pdf
- The "correct change" problem looks like it's equivalent to the "subset sum" problem, which is a special case of the knapsack problem. Wikipedia says these are all NP, but efficiency can be improved by dynamic programming. That's why I'm thinking a transposition table may help.
- Sum numbers in a list: http://stackoverflow.com/questions/3420937/algorithm-to-find-which-number-in-a-list-sum-up-to-a-certain-number
- Knapsack problem: https://en.wikipedia.org/wiki/Knapsack_problem
- PE #136, #173, and #174

### Graphs
- Pathfinding algorithm comparison: https://cstheory.stackexchange.com/questions/11855/how-do-the-state-of-the-art-pathfinding-algorithms-for-changing-graphs-d-d-l
- Shortest path algorithms: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/
- MST: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/
- Floyd Warshall algorithm: http://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm
- Dijkstra's algorithm: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

### Trees
- Balanced search trees: https://algs4.cs.princeton.edu/33balanced/
- Tree traversal construction: http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
- Determine if a tree is a BST: https://www.youtube.com/watch?v=H13iz0rbeeo
- https://en.wikipedia.org/wiki/Left-child_right-sibling_binary_tree
- https://en.wikipedia.org/wiki/AVL_tree

### Strings/arrays
- Find combinations of a string in another string: http://stackoverflow.com/questions/24720332/c-find-all-possible-combinations-of-a-string-in-another-string 
- Knuth-Morris-Pratt: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
- Rabin-Karp


## Mazes
- Think Labyrinth: http://www.astrolog.org/labyrnth/algrithm.htm
- Buckblog maze generation algorithm overview: http://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap
- Random walk: https://en.wikipedia.org/wiki/Random_walk  


## Cellular automata
- Cellular automaton: https://en.wikipedia.org/wiki/Cellular_automaton
- Elementary cellular automaton: https://en.wikipedia.org/wiki/Elementary_cellular_automaton
- Rule 30: https://en.wikipedia.org/wiki/Rule_30
- Conway's game of life: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
- Turmite: https://en.wikipedia.org/wiki/Turmite
- Wolfram cellular automata: https://www.wolframscience.com/nks/p65--more-cellular-automata/
- Nature of Code by Shiffman, chapter 7: http://natureofcode.com/book/chapter-7-cellular-automata/
- Wireworld: https://en.wikipedia.org/wiki/Wireworld
- Brian's Brain: https://en.wikipedia.org/wiki/Brian%27s_Brain
- Von Neumann: https://en.wikipedia.org/wiki/Von_Neumann_cellular_automaton
- Langton's loops: https://en.wikipedia.org/wiki/Langton%27s_loops
- CoDi: https://en.wikipedia.org/wiki/CoDi
- Life-like cellular automata (incl. Seeds): https://en.wikipedia.org/wiki/Life-like_cellular_automaton
- Interactive CA and other sundry JS animations: http://math.hws.edu/eck/js/edge-of-chaos/CA-info.html


## Compilers/interpreters
- Write a Forth interpreter:
  - Forth lang tutorial: https://www.forth.com/starting-forth/9-forth-execution/
  - Python Forth interpreter: http://openbookproject.net/py4fun/forth/forth.html
  - Easy Forth tutorial: https://skilldrick.github.io/easyforth/
- Stanford compilers courses: 
  - http://web.stanford.edu/class/archive/cs/cs143/cs143.1128/
  - https://lagunita.stanford.edu/courses/Engineering/Compilers/Fall2014/about
- Udacity programming languages course: https://classroom.udacity.com/courses/cs262
- Let's build a simple interpreter: https://ruslanspivak.com/lsbasi-part1/
- JS interpreter in JS (good for sandboxing): https://github.com/NeilFraser/JS-Interpreter
- Incremental approach to compiler construction: http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf
- Write a compiler: https://norasandler.com/2017/11/29/Write-a-Compiler.html
- Crafting Interpreters: http://craftinginterpreters.com/
- Python interpreter in Python: http://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html
- nearley/moo js: https://nearley.js.org/docs/grammar
- Compiler books: https://dickgrune.com/
- Create a simple tokenizer in C#: https://jack-vanlightly.com/blog/2016/2/3/creating-a-simple-tokenizer-lexer-in-c
- Writing your own toy compiler: https://gnuu.org/2009/09/18/writing-your-own-toy-compiler/
- Lexical analysis: https://en.wikibooks.org/wiki/Compiler_Construction/Lexical_analysis
- Simple tutorial and useful references: https://blog.mgechev.com/2017/09/16/developing-simple-interpreter-transpiler-compiler-tutorial/#references
- Simple top-down parsing: http://effbot.org/zone/simple-top-down-parsing.htm
- My first language front-end: 
  - https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html
  - https://github.com/llvm-mirror/llvm/blob/master/examples/Kaleidoscope/MCJIT/initial/toy.cpp
- Mega compilers resource: https://stackoverflow.com/questions/1669/learning-to-write-a-compiler
- CS143: https://web.stanford.edu/class/archive/cs/cs143/cs143.1128/
- Concatenative Languages: https://concatenative.org/wiki/view/Concatenative%20language


## Esoteric programming languages
- Cat's Eye: http://catseye.tc/
- Esolangs.org: https://esolangs.org/wiki/Main_Page
- Esoteric programming languages: https://en.wikipedia.org/wiki/Esoteric_programming_language
- Chess in befunge: http://www.frox25.no-ip.org/~mtve/code/eso/bef/chess/


## Game AI
- IDDFS/single agent search: http://webdocs.cs.ualberta.ca/~jonathan/PREVIOUS/Courses/657/Notes/10.Single-agentSearch.pdf
- IDA*: https://algorithmsinsight.wordpress.com/graph-theory-2/ida-star-algorithm-in-general/
- A* n puzzle: https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
- A* Jump-point search optimization: https://en.wikipedia.org/wiki/Jump_point_search
- Navmesh: https://www.cc.gatech.edu/~surban6/2019fa-gameAI/lectures/2019_08_28_searchMovement_continued2-presented%20in%20class.pdf
- Breakthrough AI tutorial: https://www.codeproject.com/Articles/37024/Simple-AI-for-the-Game-of-Breakthrough
- SSS*: https://en.wikipedia.org/wiki/SSS*
- Monte Carlo Tree Search:
  - https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/
  - http://www.baeldung.com/java-monte-carlo-tree-search
  - https://introcs.cs.princeton.edu/java/98simulation/
  - https://www.coursera.org/lecture/c-plus-plus-b/4-2-monte-carlo-a3Z4u
- Principal variation search: https://en.wikipedia.org/wiki/Principal_variation_search
- MTD-f: https://en.wikipedia.org/wiki/MTD-f
- Iterative deepening DFS: https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search
- Iterative deepening A*: https://en.wikipedia.org/wiki/Iterative_deepening_A*
- Alpha-beta pruning: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
- Tic tac toe AI: http://cwoebker.com/posts/tic-tac-toe
- Minimax: 
  - https://www.neverstopbuilding.com/blog/minimax
  - https://www.leaseweb.com/labs/2013/12/python-tictactoe-tk-minimax-ai/
- Negamax: https://en.wikipedia.org/wiki/Negamax
- Othello basic: https://inventwithpython.com/invent4thed/chapter15.html
- 4 grid games from Al Sweigart: http://inventwithpython.com/pygame/chapter10.html 
- Game of the Amazons:
  - https://www.youtube.com/watch?v=_1NzUMWeU4c
  - https://www.youtube.com/watch?v=_1NzUMWeU4c


## Games
- List of puzzle video games: https://en.wikipedia.org/wiki/List_of_puzzle_video_games
- Tile-matching video games: https://en.wikipedia.org/wiki/Tile-matching_video_game
- Microsoft Entertainment Pack: https://en.wikipedia.org/wiki/Microsoft_Entertainment_Pack
- Mahjong solitaire: https://en.wikipedia.org/wiki/Mahjong_solitaire
- 2d visibility:
  - https://www.redblobgames.com/articles/visibility/
  - http://journal.stuffwithstuff.com/2015/09/07/what-the-hero-sees/
  - https://legends2k.github.io/2d-fov/design.html
  - In Phaser using a raycasting lib: https://www.emanueleferonato.com/2015/02/03/play-with-light-and-dark-using-ray-casting-and-visibility-polygons/
- 3d Wolfenstein raycasting tutorial in JS: https://dev.opera.com/articles/3d-games-with-canvas-and-raycasting-part-1/  
- Minichess: https://en.wikipedia.org/wiki/Minichess
- Minesweeper with hex grid (try tri grid as well): https://www.redblobgames.com/grids/hexagons/
- Dots and boxes: https://www.youtube.com/watch?v=KboGyIilP6k
- Breakthru: https://en.wikipedia.org/wiki/Breakthru_(board_game)
- Beast: https://en.wikipedia.org/wiki/Beast_(video_game)
- Program arcade games: http://programarcadegames.com/
- BASIC games: http://www.atariarchives.org/basicgames/
- Nim: https://en.wikipedia.org/wiki/Nim
- Emily's pegs game: http://www.instructables.com/id/Peg-Game-IQ-Test-Solution/
- Fire & Ice: https://www.youtube.com/watch?v=1t782B0zK3Y
- Filler/Qualio: https://www.youtube.com/watch?v=WV-rQfYKSGA
  - Generating levels: https://stackoverflow.com/questions/59692024
- Tower defense
- Hexapawn: https://en.wikipedia.org/wiki/Hexapawn
- Octopawn
- Pipe Dream: https://en.wikipedia.org/wiki/Pipe_Mania
- Quarto: https://boardgamegeek.com/boardgame/681/quarto
- Mancala: https://en.wikipedia.org/wiki/Mancala
- Jezzball: https://en.wikipedia.org/wiki/JezzBall
- Freerice clone
- Patience: https://en.wikipedia.org/wiki/Patience_(game)
- Hex: https://en.wikipedia.org/wiki/Hex_(board_game)
- Lines of action: https://dke.maastrichtuniversity.nl/m.winands/loa/
- Boulder Dash: https://en.wikipedia.org/wiki/Boulder_Dash
- Ultimate tic tac toe or other variants: https://en.wikipedia.org/wiki/Tic-tac-toe_variants
- Marble Madness: https://en.wikipedia.org/wiki/Marble_Madness
- Loco-Motion: https://en.wikipedia.org/wiki/Loco-Motion_(video_game)
- Digger: https://en.wikipedia.org/wiki/Digger_(video_game)
- Nine Men's Morris: https://en.wikipedia.org/wiki/Nine_Men%27s_Morris
- Rummikub: https://en.wikipedia.org/wiki/Rummikub
- Hnefatafl
- Hive
- Go
- 2048
- Boggle
- Lemmings
- Snake: 2 player versions, add obstacles, snake tetris, ai
  - https://johnflux.com/2015/05/02/nokia-6110-part-3-algorithms/
  - https://towardsdatascience.com/slitherin-solving-the-classic-game-of-snake-with-ai-part-3-genetic-evolution-33186e6be110
- Solved games list: https://en.wikipedia.org/wiki/Solved_game
- Mastermind: https://en.wikipedia.org/wiki/Mastermind_(board_game)
- Open souce game clones: https://osgameclones.com/
- List of abstract strategy games: https://en.wikipedia.org/wiki/List_of_abstract_strategy_games
- Reversi: http://inventwithpython.com/chapter15.html
- Checkers, misere checkers and variants:
  - https://boardgamegeek.com/geeklist/147417/best-checkers-variants
  - http://www.di.fc.ul.pt/~jpn/gv/checkers.htm
  - https://en.wikipedia.org/wiki/Draughts#Invented_variants
- ASCII games: 
  - http://ifarchive.org/
  - http://www.8bs.com/othrdnld/manuals/publications.shtml
  - https://en.wikipedia.org/wiki/Jotto
  - https://en.wikipedia.org/wiki/NetHack
  - http://www.iancgbell.clara.net/elite/text/index.htm
  - MUDS such as God Wars
- Interactive fiction:
  - Knuth adventure: http://literateprogramming.com/adventure.pdf
  - TADS3: https://www.tads.org/
- Tile-based game tutorial: https://www.youtube.com/watch?v=txUvD5_ROIU  
- Puzzlescript: 
  - Tumblr: https://puzzlescriptgallery.tumblr.com/
  - Itch: https://itch.io/games/made-with-puzzlescript


## Puzzles
- Logic puzzles list (KenKen, Sudoku, Sokoban, etc): https://en.wikipedia.org/wiki/Category:Logic_puzzles
- Simon Tatham: https://www.chiark.greenend.org.uk/~sgtatham/puzzles/
- Do chess packing puzzles
- Erich Friendman's Puzzle Palace: http://www2.stetson.edu/~efriedma/
- Slitherlink: https://en.wikipedia.org/wiki/Slitherlink
- Mindsports (links resource): http://www.mindsports.nl/index.php/puzzle-links
- Zendoku puzzle generation: http://garethrees.org/2007/06/10/zendoku-generation/#section-4
- Sudoku solving algorithms: https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
- Generating sudoku boards: https://stackoverflow.com/questions/6924216/how-to-generate-sudoku-boards-with-unique-solutions
- Mondrian puzzle: https://www.youtube.com/watch?v=49KvZrioFB0
- Various puzzles from the Sudoku inventors: http://nikoli.co.jp/en/puzzles/
- Peter Norvig on Sudoku and other constraint problems (such as the skyscraper puzzle): http://norvig.com/sudoku.html
- More constraint puzzles: https://www.wikihow.com/Solve-a-Magnets-Puzzle
- Nonogram: https://en.wikipedia.org/wiki/Nonogram
- Ricochet Robots: https://en.wikipedia.org/wiki/Ricochet_Robot
- Slothouber-Graatsma puzzle: https://en.wikipedia.org/wiki/Slothouber%E2%80%93Graatsma_puzzle 
- Packing: https://en.wikipedia.org/wiki/Packing_problems
- Triomino packing: https://www.youtube.com/watch?v=hW4nB-ZAhts
- Irregular hexagon packing: https://www.youtube.com/watch?v=i_TU49MioEE
- Mathematical puzzle: https://en.wikipedia.org/wiki/Mathematical_puzzle
- Soma cube: https://en.wikipedia.org/wiki/Soma_cube
- Assorted logic games: https://www.youtube.com/channel/UCEPZPgtnTvj2F3qTCLfaP4w
- Lights Out: https://en.wikipedia.org/wiki/Lights_Out_(game)
- A bunch of puzzle games: http://www.puzzle-bridges.com/
- Dissection puzzle: https://en.wikipedia.org/wiki/Dissection_puzzle
  - https://www.youtube.com/watch?v=P-9qBV-9Fos
- Tangram: https://en.wikipedia.org/wiki/Tangram 
- Klotski gone insane (Bricks game): http://www.bricks-game.de/
- TopSpin and other puzzles:
  - https://www.jaapsch.net/puzzles/topspin.htm
  - https://www.jaapsch.net/


## Fractals and L-systems
- Algorithmic Botany: http://algorithmicbotany.org/
- Space colonization: https://www.youtube.com/watch?v=kKT0v3qhIQY&index=20&list=PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH
- Paul Bourke: http://paulbourke.net/fractals/
- Book on JS fractals: http://www.playingwithchaos.net/
- L-systems user notes/manual: http://paulbourke.net/fractals/lsys/
- L-system examples: https://10klsystems.wordpress.com/examples/
- 2d L-systems: http://mathforum.org/advanced/robertd/lsys2d.html
- Harriss spiral: http://fiys169.blogspot.com/2015/11/the-harriss-spiral.html
- Full-featured L-systems app: http://www.kevs3d.co.uk/dev/lsystems/
- Hausdorff fractals list: https://en.wikipedia.org/wiki/List_of_fractals_by_Hausdorff_dimension
- Abelian sandpiles: https://en.wikipedia.org/wiki/Abelian_sandpile_model 
- Koch snowflake: https://en.wikipedia.org/wiki/Koch_snowflake
- Sierpinski carpet: https://en.wikipedia.org/wiki/Sierpinski_carpet
- Haferman Carpet: http://mathworld.wolfram.com/HafermanCarpet.html
- Rose: https://en.wikipedia.org/wiki/Rose_(mathematics)
- Chaos game: https://en.wikipedia.org/wiki/Chaos_game
- Barnsley Fern: https://en.wikipedia.org/wiki/Barnsley_fern


## Visual/animation
- Inspiring zreference projects: http://zreference.com/projects/graphics/
- Also inspiring, bit101 dailies: https://bit101.github.io/lab/dailies/170413.html
- Handbook of Graph Drawing and Visualization: http://cs.brown.edu/people/rtamassi/gdhandbook/
- Convex hull: 
  - https://en.wikipedia.org/wiki/Convex_hull_algorithms
  - https://en.wikipedia.org/wiki/Orthogonal_convex_hull
- Delaunay triangulation:
  - https://transcendentcode.wordpress.com/2014/01/26/triangulation/
  - https://en.wikipedia.org/wiki/Delaunay_triangulation
  - http://www.geom.uiuc.edu/~samuelp/del_project.html#algorithms
  - https://en.wikipedia.org/wiki/Voronoi_diagram#Algorithms
- Graph drawing: https://en.wikipedia.org/wiki/Graph_drawing
- Isometric:
  - https://stackoverflow.com/questions/892811/drawing-isometric-game-worlds
  - http://www.gamedesign.jp/flash/slidingblock/slidingblock.html
- goto80 ASCII art: http://goto80.com/chipflip/06/
- Fibonacci spiral: https://en.wikipedia.org/wiki/Fibonacci_number
- Architecture: look for triangle perspective designs, Escher: https://s-media-cache-ak0.pinimg.com/564x/d6/ff/64/d6ff6450173c6410c919b06e07958227.jpg
- Do a visual plotting the orthocenter, medicenter, and circumcenter of a triangle
- Write a script that turns text into blocky ASCII text or renders images in ASCII
- JSXGraph: https://jsxgraph.uni-bayreuth.de/wiki/index.php/Category:Examples
- Bezier Curves:
  - A Primer on Bezier Curves: https://pomax.github.io/bezierinfo/
  - Bezier curve tool: http://www.victoriakirst.com/beziertool/
  - Chaining Bezier curves: 
    - http://html5tutorial.com/how-to-join-two-bezier-curves-with-the-canvas-api/
    - http://www.algosome.com/articles/continuous-bezier-curve-line.html
    - https://stackoverflow.com/questions/12295773/joining-two-b%C3%A9zier-curves-smoothly-c2-continuous
    - https://www.cl.cam.ac.uk/teaching/2000/AGraphHCI/SMEG/node3.html
    - https://en.wikipedia.org/wiki/Composite_B%C3%A9zier_curve
    - https://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/Bezier/bezier-der.html
- Splines intro: https://www.ibiblio.org/e-notes/Splines/Intro.htm
- Canvas stack: http://arc.id.au/CanvasLayers.html
- Create gif from a canvas animation: https://stackoverflow.com/questions/10486084/generate-animated-gif-with-html5-canvas
- Animate the Collatz Conjecture
- ReCode Project (computer art repository): https://mepler.com/The-ReCode-Project
- CompArt: http://dada.compart-bremen.de
- The Algorists: http://algorists.org/algorist.html
- Sol LeWitt: https://en.wikipedia.org/wiki/Sol_LeWitt
- 3d sombrero and other algorithms: https://js.do/samples/sombrero
- Necessary Disorder: https://necessarydisorder.wordpress.com/2017/11/15/drawing-from-noise-and-then-making-animated-loopy-gifs-from-there/
- ThreeJS fundamentals: https://threejsfundamentals.org/
- Mr. Doob three.js collection: http://mrdoob.com/


### WebGL
- The book of shaders: https://thebookofshaders.com/
- WebGL tutorial: https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tutorial
- Try out regl: https://bits.coop/articles/rigging-and-animation/
- https://github.com/regl-project/regl
- https://github.com/regl-project/awesome-regl
- http://regl.party/api
- Erkaman: https://github.com/Erkaman
- An Intro to regl for Data Visualization: https://vallandingham.me/regl_intro.html


## Tiling and packing
- Lubachevsky packing algorithm: https://en.wikipedia.org/wiki/Lubachevsky%E2%80%93Stillinger_algorithm
- Rhombile tiling: https://en.wikipedia.org/wiki/Rhombille_tiling
- Tangrams: https://en.wikipedia.org/wiki/Tangram
- Tiling puzzle: https://en.wikipedia.org/wiki/Tiling_puzzle
- L-systems in inkscape: https://thebrickinthesky.wordpress.com/2013/03/17/l-systems-and-penrose-p3-in-inkscape
- Girih tiles: https://en.wikipedia.org/wiki/Girih_tiles
- Wallpaper group: https://en.wikipedia.org/wiki/Wallpaper_group
- Morphing Tiling: https://morphingtiling.wordpress.com/page/2/
- Transcendent Code: https://transcendentcode.wordpress.com/
- Penrose tiling: 
  - http://preshing.com/20110831/penrose-tiling-explained/ 
  - http://www.math.ubc.ca/~cass/courses/m308-02b/projects/schweber/penrose.html
- Substitution tiling: https://en.wikipedia.org/wiki/Substitution_tiling
- "Isometic" JS example: http://jsfiddle.net/a4ZbG/
- Triaki's: https://en.wikipedia.org/wiki/Truncated_hexagonal_tiling#Triakis_triangular_tiling
- Litema: https://en.wikipedia.org/wiki/Litema
- Kuba textiles: https://en.wikipedia.org/wiki/Kuba_textiles
- Jason Davies: https://www.jasondavies.com/
- Circle packing flickr: https://www.flickr.com/photos/quasimondo/albums/72157624374940604


## Physics simulations
- Falling sand game: https://en.wikipedia.org/wiki/Falling-sand_game
- Cloth physics: https://andrew.wang-hoyer.com/experiments/cloth/
- Verlet integration: https://www.youtube.com/watch?v=3HjO_RGIjCU
- Ragdoll physics: https://en.wikipedia.org/wiki/Ragdoll_physics
- Coding math tutorial: https://www.youtube.com/watch?v=11ZmRlR7sOQ 
- Khan Academy natural simulations course: https://www.khanacademy.org/computing/computer-programming/programming-natural-simulations/programming-vectors/p/project-computational-creatures
- Double pendulum: 
  - Coding challenge 93: https://www.youtube.com/watch?v=uWzPe_S-RVE&t=0s&list=PLRqwX-V7Uu6ZiZxtDDRCi6uhfTH4FilpH&index=131
  - https://en.wikipedia.org/wiki/Double_pendulum 
  - https://www.youtube.com/watch?v=neh86u7_TIk
- Game physics cookbook: http://proquest.safaribooksonline.com/9781787123663
- Jansen's linkage: https://en.wikipedia.org/wiki/Jansen%27s_linkage
- Nature in Code book: https://leanpub.com/natureincode
- Sin & cos:  
  - Brief intro to sin & cos: https://inventwithpython.com/blog/2012/07/18/using-trigonometry-to-animate-bounces-draw-clocks-and-point-cannons-at-a-target/
  - and another intro to sin & cos with some mode 7 content: http://www.helixsoft.nl/articles/circle/sincos.htm
- Circles bouncing off lines tutorial: https://circles-bouncing-off-lines.glitch.me/docs/circles-bouncing-off-lines.html
- Mary Rose Cook: https://maryrosecook.com/
- Flocking behaviors: http://harry.me/blog/2011/02/17/neat-algorithms-flocking/
- Math for game developers: https://www.youtube.com/playlist?list=PLW3Zl3wyJwWOpdhYedlD-yCB7WQoHf-My
- Variety of pathfinding tutorials: https://www.redblobgames.com/pathfinding/a-star/introduction.html 
- Blobs: http://cowboyprogramming.com/2007/01/05/blob-physics/
- Various tutorials for 2d graphics (isometric, polygon, collision, platformers, networking, etc): https://2dengine.com/?p=tutorials 
- Simple 2d physics engine: https://www.ibm.com/developerworks/library/wa-build2dphysicsengine/
- 2d physics engine 3 part tutorial: http://hugobdesigner.blogspot.com/
- Pool hall physics: https://www.gamasutra.com/view/feature/131424/pool_hall_lessons_fast_accurate_.php?print=1
- Collision detection:
  - http://www.dyn4j.org/2010/01/sat/
  - https://gamedevelopment.tutsplus.com/tutorials/collision-detection-using-the-separating-axis-theorem--gamedev-169
  - https://wildbunny.co.uk/blog/2011/04/20/collision-detection-for-dummies/
  - https://www.codeproject.com/Articles/15573/2D-Polygon-Collision-Detection
  - https://stackoverflow.com/questions/10962379/how-to-check-intersection-between-2-rotated-rectangles/12414951#12414951
  - https://github.com/antishow/collision-demo/tree/master/library/js/src
  - http://paulbourke.net/fractals/randomtile/
  - https://maryrosecook.com/blog/post/how-to-do-2d-collision-detection
  - http://www.metanetsoftware.com/technique/tutorialA.html
  - http://www.migapro.com/circle-and-rotated-rectangle-collision-detection/
  - https://gist.github.com/eliasdaler/502b54fcf1b515bcc50360ce874e81bc
  - https://gist.github.com/cwleonard/e124d63238bda7a3cbfa
  - https://gist.github.com/LindseyB/394536
  - https://gist.github.com/enghqii/5af2512ced10849016e635fcf2d15d29
  - https://github.com/tetoblivion/Collision_response_with_rotation/blob/master/respondToCollision.cpp
  - https://gamedev.stackexchange.com/questions/32611/what-is-the-best-way-to-handle-simultaneous-collisions-in-a-physics-engine
- Quadtrees: 
  - https://en.wikipedia.org/wiki/Quadtree
  - https://gamedevelopment.tutsplus.com/tutorials/quick-tip-use-quadtrees-to-detect-likely-collisions-in-2d-space--gamedev-374


## Regex 
- Advanced regex features ref sheet: https://www.regular-expressions.info/refadv.html
- Regex Static Analysis: http://www.cs.sun.ac.za/~abvdm/regex.html
- Catastrophic Backtracking: https://www.regular-expressions.info/catastrophic.html
- Implementing Regular Expressions: https://swtch.com/~rsc/regexp/
- Write a regex engine: https://rcoh.me/posts/no-magic-regular-expressions/
- Mini regex: https://learning.tarokuriyama.com/2020/02/mini-regex.html
- Replace with conditional: https://www.regular-expressions.info/replaceconditional.html 
- True power of regex: http://nikic.github.io/2012/06/15/The-true-power-of-regular-expressions.html


## Operating Systems
- CS4210 archive: https://www.cc.gatech.edu/classes/AY2010/cs4210_fall/
- Operating Systems notes: https://www2.cs.uic.edu/~jbell/CourseNotes/OperatingSystems/
- OS @ NYU: https://cs.nyu.edu/~mwalfish/classes/ut/s11-cs372h/hw/sol8.html
- Berkeley CS162: https://cs162.eecs.berkeley.edu/
- What every programmer should know about memory: https://akkadia.org/drepper/cpumemory.pdf
- The Little Book of Semaphores: https://greenteapress.com/wp/semaphores/
- Computer Systems: A Programmer's Perspective: https://csapp.cs.cmu.edu/


## Computer Science
- CS SE FAQ: https://cs.meta.stackexchange.com/questions/599/reference-answers-to-frequently-asked-questions/847#847
- Rick Hehner's top 10: http://www.cs.toronto.edu/~hehner/best.html
- Software foundations book series: https://softwarefoundations.cis.upenn.edu/
- JFLAP: http://www.jflap.org/
- SAT SMT by Example: https://yurichev.com/writings/SAT_SMT_by_example.pdf


## Machine learning
- Deep Learning book: http://www.deeplearningbook.org/
- wasd12345 on GitHub: https://github.com/wasd12345


## AI
- Berkeley CS188 AI with Pacman: http://ai.berkeley.edu/project_overview.html
- Intro to Intelligent Systems: https://www.cs.rit.edu/~rlc/Courses/IS/


## Cryptography
- https://crypto.stanford.edu/~dabo/cryptobook/BonehShoup_0_4.pdf
- DH key exchange in plain English: http://security.stackexchange.com/questions/45963/diffie-hellman-key-exchange-in-plain-english


## Data science
- APIs/Datasets
  - https://github.com/toddmotto/public-apis 
  - https://github.com/public-apis/public-apis/blob/master/README.md 
  - https://apilist.fun/
  - https://www.quora.com/What-are-some-cool-fun-random-APIs-such-as-BreweryDB 
  - https://botwiki.org/resources/datasets/
  - https://botwiki.org/resources/apis/ 
  - https://randomuser.me/api/?results=100 
  - unsplash photo API: https://github.com/MuseumofModernArt/exhibitions 
  - makeup: http://makeup-api.herokuapp.com/  
  - diatoms: https://diatoms.org/species  
  - https://github.com/awesomedata/awesome-public-datasets 
  - https://github.com/mwaskom/seaborn-data
  - R datasets: https://vincentarelbundock.github.io/Rdatasets/datasets.html  
  - data.gov: https://catalog.data.gov/dataset?tags=plants
  - CIA world factbook:
    - https://github.com/thewiremonkey/factbook.csv
    - https://www.cia.gov/library/publications/the-world-factbook/
  - https://github.com/erikgahner/PolData/blob/master/PolData.csv
  - https://github.com/jldbc/gunsandcrime
  - https://gist.github.com/klmr/23ed79f973c75b11b0b5
  - https://www.washingtonpost.com/wp-srv/health/interactives/guns/ownership.html
  - https://restcountries.eu/
  - https://rel.ink/
  - https://pipedream.com/
  - https://example-data.draftbit.com/
  - https://github.com/vera-institute/incarceration_trends
- Inspirational projects:
  - https://douweosinga.com/projects/


## C
- Build your own lisp: http://www.buildyourownlisp.com/
- Write your own OS: https://wiki.osdev.org/Tutorials
- Beej guide to GDB: https://beej.us/guide/bggdb/
- C coding standard: https://barrgroup.com/Embedded-Systems/Books/Embedded-C-Coding-Standard
- C IAQ: http://www.seebs.net/faqs/c-iaq.html 


## C++
- C++ SFML for games and graphics
- Async C++ tutorial: https://solarianprogrammer.com/2012/10/17/cpp-11-async-tutorial/


## JS
- Dwitter (140 chars or less JS code): https://www.dwitter.net/ 
- 30 day vanilla JS challenge: https://javascript30.com/
- JS todo list: http://docs.railsbridge.org/javascript-to-do-list/adding_an_item
- https://codeburst.io/getting-started-with-react-router-5c978f70df91
- https://react-redux.js.org/introduction/quick-start
- https://www.leighhalliday.com/async-axios-react-testing-library
- https://github.com/testing-library/react-testing-library#hooks
- https://levelup.gitconnected.com/testing-asynchronous-and-synchronous-react-components-with-jest-and-enzyme-a979ab425aa1


## Web development
- Jekyll blog: 
  - https://www.youtube.com/watch?v=xdxfyFS3pog
  - https://jekyllrb.com/docs/installation/
- Bitballoon for hosting web apps: https://www.bitballoon.com

### CSS
- Do a Mondrian generator with a CSS grid or JS
- Grid: https://css-tricks.com/snippets/css/complete-guide-grid/
- Rachel Andrew (CSS grid examples): https://codepen.io/rachelandrew/pens/public
- CSS cube: https://davidwalsh.name/css-cube


## Python
- Write a Lisp interpreter in Python: http://norvig.com/lispy.html
- Host a free Python web app: https://www.pythonanywhere.com/
- Natural language processing with Python: http://www.nltk.org/book/
- Pygame: http://inventwithpython.com/pygame/
- Automate the boring stuff: https://automatetheboringstuff.com/
- Simple Python graphics library: https://www.rose-hulman.edu/Users/faculty/young/CS-Classes/resources/Python/ZelleGraphics.html
- Flask:
  - https://exploreflask.com/en/latest/
  - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
  - http://charlesleifer.com/blog/how-to-make-a-flask-blog-in-one-hour-or-less/
- Python data structures & algorithms
  - http://interactivepython.org/runestone/static/pythonds/index.html
  - http://www.brpreiss.com/books/opus7/
- Computer vision with python: http://programmingcomputervision.com/downloads/ProgrammingComputerVision_CCdraft.pdf
- Effective Python: http://www.effectivepython.com/
- How to think like a computer scientist: http://interactivepython.org/courselib/static/thinkcspy/index.html
- Python Challenge: http://pythonchallenge.com/
- Tkinterbook: http://effbot.org/tkinterbook/


## PHP
- Sessions/logins:
  - http://culttt.com/2013/02/04/how-to-save-php-sessions-to-a-database/
  - http://shiflett.org/articles/storing-sessions-in-a-database
  - http://php.net/manual/en/function.session-set-save-handler.php
  - https://www.sitepoint.com/writing-custom-session-handlers/
  - https://github.com/sprain/PHP-MySQL-Session-Handler/blob/master/MySqlSessionHandler.php
  - https://github.com/JamieCressey/PHP-MySQL-Session-Handler
  - https://github.com/kahwee/php-db-session-handler
  - https://www.allphptricks.com/simple-user-registration-login-script-in-php-and-mysqli/
  - https://phpeasystep.com/workshopview.php?id=6
  - http://www.eggslab.net/php-login-script/
  - http://codewithawa.com/posts/admin-and-user-login-in-php-and-mysql-database
  - https://www.formget.com/login-form-in-php/
- PHP game scripts: https://www.ibm.com/developerworks/library/os-php-gamescripts1/
- Websocket chat: https://phppot.com/php/simple-php-chat-using-websocket/
- PHP Sadness: http://phpsadness.com/


## Java
- Google style guide: https://google.github.io/styleguide/javaguide.html
- Good Java web framework for learning generics: https://struts.apache.org/ 
- Java sorting algorithms: http://java2novice.com/java-sorting-algorithms/
- Java send HTTP request: http://stackoverflow.com/questions/2793150/using-java-net-urlconnection-to-fire-and-handle-http-requests
- Java send email: http://stackoverflow.com/questions/3649014/send-email-using-java


## Ruby
- Why's Poignant Guide to Ruby: http://poignant.guide/book/chapter-6.html
- Nice Ruby regex tutorial: http://ruby-doc.com/docs/ProgrammingRuby/html/tut_stdtypes.html
- Programming Ruby: http://ruby-doc.com/docs/ProgrammingRuby/html/rubyworld.html


## Perl
- Perl data structures cookbook: http://perldoc.perl.org/perldsc.html


## MIPS
- MIPS system calls: http://students.cs.tamu.edu/tanzir/csce350/reference/syscalls.html
- Learning MIPS and SPIM: https://uweb.engr.arizona.edu/~ece369/Resources/spim/QtSPIM_examples.pdf
- recursion: https://courses.engr.illinois.edu/cs232/sp2012/section/disc2sol.pdf
- https://courses.cs.washington.edu/courses/cse378/09wi/lectures/lec05.pdf
- https://en.wikibooks.org/wiki/MIPS_Assembly/Control_Flow_Instructions
- https://www.coursehero.com/file/45823007/cs311-03-isa-Ipdf/
- https://github.com/kyungyunlee/CS311-Computer-Organization/tree/master/project2/Project2
- https://github.com/mightydeveloper/MIPS-Assembler
- https://www.youtube.com/watch?v=z3ltaJ5UU5I
- https://learnxinyminutes.com/docs/mips/
- https://chortle.ccsu.edu/AssemblyTutorial/index.html
- http://www.cs.uwm.edu/classes/cs315/Bacon/Lecture/HTML/ch05s03.html
- http://homepage.divms.uiowa.edu/~ghosh/1-28-10.pdf
- http://cgi.cse.unsw.edu.au/~cs1521/17s2/docs/spim.php
- https://www.dsi.unive.it/~gasparetto/materials/MIPS_Instruction_Set.pdf
- https://www.doc.ic.ac.uk/lab/secondyear/spim/node9.html
- https://www.doc.ic.ac.uk/lab/secondyear/spim/node20.html
- https://www.math.unipd.it/~sperduti/ARCH09/mips_assembler.pdf
- http://www.mrc.uidaho.edu/mrc/people/jff/digital/MIPSir.html



## ARM
- Thinkingeek Raspberry Pi Asssembler: 
  - Site: https://thinkingeek.com/2013/01/09/arm-assembler-raspberry-pi-chapter-1/
  - eBook: https://personal.utdallas.edu/~pervin/RPiA/RPiA.pdf
- ARM Assembly Using Raspberry PI: http://www.microdigitaled.com/ARM/ASM_ARM/Software/ARM_Assembly_Programming_Using_Raspberry_Pi_GUI.pdf
- Smith College ARM Tutorial: http://www.science.smith.edu/dftwiki/index.php/Tutorial:_Assembly_Language_with_the_Raspberry_Pi
- Hello ARM: http://www.bravegnu.org/gnu-eprog/hello-arm.html
- Tutorials: 
  - https://www.youtube.com/watch?v=5HILZon7pVE
  - https://www.youtube.com/watch?v=zl04ZfdkiuM
  - https://www.youtube.com/watch?v=1VAcZr2wQzo


## Raspberry Pi
- Extending the life of the SD card:
  - https://domoticproject.com/extending-life-raspberry-pi-sd-card/
  - https://raspberrypi.stackexchange.com/questions/169/how-can-i-extend-the-life-of-my-sd-card


## Unix
- Bandit wargames: http://overthewire.org/wargames/bandit/
- Learn vim script: http://learnvimscriptthehardway.stevelosh.com/


## Prolog 
- FSAs in Prolog: http://cs.union.edu/~striegnk/courses/nlp-with-prolog/html/node5.html#l1.prolog
- 99 prolog problems: https://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/


## Code golf
- code-golf.io: https://code-golf.io/
- js1k: https://js1k.com/
- https://js1024.fun/
- anarchy golf: http://golf.shinh.org/
- Perlgolf history: http://terje2.frox25.no-ip.org/perlgolf_history_070109.pdf


## Scratch/Snap
- Sulfurous: https://sulfurous.aau.at/
- Useful Scratch reference topics: 
  - https://wiki.scratch.mit.edu/wiki/Array#Multidimensional_Arrays_in_Scratch
  - https://wiki.scratch.mit.edu/wiki/List_of_Mathematical_Functions_Done_in_Scratch
  - https://wiki.scratch.mit.edu/wiki/Recursion_and_Fractals#Creating_the_Koch_Curve
- Snap instead of Scratch: http://www.ocsmag.com/2016/07/12/dump-scratch-use-blockly-or-snap-instead/
- Multiwingspan projects: http://www.multiwingspan.co.uk/scratch.php?page=ex1


## Course sites
- Nand2Tetris: http://nand2tetris.org/
- Coding the Matrix (linear algebra through CS): http://codingthematrix.com/
- Advanced Web Developer Bootcamp: https://www.udemy.com/the-advanced-web-developer-bootcamp/
- Lynda SFPL: https://www.lynda.com/portal/patron?org=sfpl.org
- Coursera algorithms classes (pts 1 & 2): https://www.coursera.org/learn/algorithms-part1
- Egghead: https://egghead.io/
- Udacity intro to theoretical CS: https://www.udacity.com/course/intro-to-theoretical-computer-science--cs313
- Jeff Erickson's algorithms: http://jeffe.cs.illinois.edu/teaching/algorithms/
- UW Data Structures & Algorithms: https://courses.cs.washington.edu/courses/cse326/03wi/326lecturesa.shtml
- Math: 
  - MIT OCW Math for CS: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/
  - FSU Discreet Math I: https://www.math.fsu.edu/~pkirby/mad2104/SlideShow/CourseNotesMAD2104.pdf
  - Calculus for beginners: http://www-math.mit.edu/~djk/calculus_beginners/
  - https://www.calculusexpert.com/library/ 
  - http://www.mathmeetsyou.com/home/trigonometry
  - http://www.greenteapress.com/thinkbayes/html/index.html
  - https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/


## Algorithmic challenge sites
- Google Code Jam: https://code.google.com/codejam/past-contests
  - Go-Hero: https://www.go-hero.net/jam/16/ has archive all the past Google Code Jam problems w/ solutions
- Daily Programmer: https://www.reddit.com/r/dailyprogrammer/
- Math problems: https://www.mathworks.com/matlabcentral/cody/problems
- Learneroo: https://www.learneroo.com/
- Topcoder: https://www.topcoder.com/getting-started
- Hacker Earth: https://www.hackerearth.com/challenges/
- Code chef: https://www.codechef.com/
- SPOJ: http://www.spoj.com/
- Exercism: http://www.exercism.io
  - Talk on exercism: https://www.youtube.com/watch?v=neXJOhHj8ik&index=6&list=PLyGLemjnH3ukTGW8TYCzdu7jQe0U-wEKi
- Kattis: https://kattis.com
- Coding Bat: http://codingbat.com
- Timus: https://acm.timus.ru/
- Code kata: http://codekata.pragprog.com/
- Root me: https://www.root-me.org/en/Challenges/Web-Client/Javascript-Native-code


## Competitive coding
- CSES: https://cses.fi/
- Competitive Programmer's Handbook: https://cses.fi/book/book.pdf
- Introduction to programming contests: http://web.stanford.edu/class/cs97si/
- Codeforces: http://codeforces.com/
- Topcoder: https://www.topcoder.com/community/competitive-programming/
- Tons of tips & links: http://www.pvv.ntnu.no/~spaans/programming.html
- Hacking competition for kids: https://picoctf.com/
- SWERC past problem sets: https://swerc.eu/2017/problems/


## Books 
- Definitive C++ book list: https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list
- Tons of free CS books: http://proquest.safaribooksonline.com/
- Think Bayes/DSP/Complexity/OS/etc: http://www.greenteapress.com/thinkbayes/html/index.html
- Fuzzing book (software testing): https://www.fuzzingbook.org/
- "Book of Proof" Hammack
- Discrete Math: http://discrete.openmathbooks.org/dmoi3.html
- Craft of Text Editors: http://www.finseth.com/craft/index.html


## Education
- SFSU
  - http://bulletin.sfsu.edu/colleges/science-engineering/computer-science/ms-computer-science/
  - Prospective students are welcome to send any questions to the graduate advising assistant at (csgrad@sfsu.edu)
- VT: http://www.vtmit.vt.edu/
- Bootcamps: http://getcoding.hackreactor.com/remote-part-time
- Internships:
  - https://www.indeed.com/q-Software-Engineering-Intern-l-San-Francisco-Bay-Area,-CA-jobs.html
  - http://www.engineerjobs.com/internships/software-engineering/california/bay-area.php
  - https://www.smartrecruiters.com/Line2/112808690-web-developer-internship-front-end
- Mills: https://www.mills.edu/academics/graduate-programs/computer-science/
- CSU Fullerton: https://www.calstateonline.net/Cal-State-Campuses/CSU-Fullerton
- Adv. certif. in web/mobile via SDSU: https://www.ces.sdsu.edu/science-computers-technology/advanced-certificate-web-and-mobile-applications-development
- Northeastern Silicon Valley: http://www.northeastern.edu/siliconvalley/admissions/
- College choice CS: https://www.collegechoice.net/rankings/best-online-masters-in-computer-science/
- Recurse non-bootcamp: https://www.recurse.com/


## OMSCS

- Course syllabi: https://drive.google.com/drive/u/0/folders/1ELjIQBaekmSF0fspJn4W7iuOWh3UxYN_

### Tier 1
- Fall 20:  
  - ISYE 6501 Intro to Analytics Modeling
- Spring 21:
  - CSE 6220 Intro to High Performance Computing: https://www-users.cs.umn.edu/~karypis/parbook/
- Summer 21:
  - CS 6515 Graduate Algorithms
    - https://gt-algorithms.com/
    - https://cs170.org/
    - http://omscs.wikidot.com/courses:cs6515
    - https://teapowered.dev/assets/ga-notes.pdf
 
### Tier 2
- CS 6265 Information Security Lab
  - https://tc.gts3.org/cs6265/2020-spring/cal.html
  - http://phrack.com
- CS 6250 Computer Networks
  - prereq course: https://www.cc.gatech.edu/~rama/CS2200-External/
  - more prereq/alternate suggestions: https://github.com/ossu/computer-science/issues/520
- CS 6460 Educational Technology
- CS 6260 Applied Cryptography
  - https://teapowered.dev/assets/crypto-notes.pdf
- ISYE 6644 Simulation
- CS 6601 Artificial Intelligence
- interesting 6310 textbooks worth looking into: https://www.reddit.com/r/OMSCS/comments/a445mn/can_you_recommend_textbooks_for_the_cs_6300_6310/

### Completed
- Fall 18: CS 6200 Intro to Operating Systems
- Spring 19: CS 6210 Advanced Operating Systems 
- Summer 19: CS 6340 Software Analysis and Test
  - Static Program Analysis (main text): https://cs.au.dk/~amoeller/spa/
  - Relevant books: https://d1b10bmlvqabco.cloudfront.net/attach/jbe3aw2nwc031n/ixory6sosP2/jcigv7z03w61/books.pdf
  - Course website: http://rightingcode.org/
  - Nice follow-up Udacity course: https://classroom.udacity.com/courses/cs259
- Fall 19: CS 6290 High Performance Computer Architecture
- Spring 20: CS 8803-O08 Compilers
- Spring 20: CS 6291 Embedded Systems Optimization
- Summer 20: CS 7638 AI for Robotics
  - https://teapowered.dev/assets/ai4r-notes.pdf


## CCSF
- CCSF Coders resources page: https://github.com/CCSF-Coders/learning-resources
- CS211s notes: https://sites.google.com/site/koalalearn/fa2011/cs211s

### CCSF courses to take
- CS   177   Software Engineering
- CS   231   Advanced Python Programming
- CS   211D  Android Programming
- CS   211E  Advanced Java: Enterprise Edition
- CS   270   Comp Architecture w/ Assembly (advise discrete math)
- CS   150P  SQL Server T-SQL Programming  
- CS   155B  MySQL Database Administration
- CS   260A  Linux System Administration
- CS   260P  Linux Administration Projects  
- CS   197P  Technical Interview Prep
- CS   197V  Version Control & Code Repos
- CS   199   Independent Study
- CS   256   Data Visualization 
- CNIT 141   Cryptography For Computer Networks
- CNIT 123   Ethical Hacking
- CNIT 124   Adv. Ethical Hacking
- CNIT 127   Exploit Development
- MATH  80   Probability and Statistics 
- MATH  95   Trigonometry
- MATH 110A  Calculus I 
- MATH 115   Discrete Mathematics 
- MATH 120   Linear Algebra

### CCSF certificates I've attained:
  - Java: https://www.ccsf.edu/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerScience/ComputerProgrammingJavaCertificate.pdf
  - Web application programming: http://www.ccsf.edu/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerScience/WebApplicationProgrammingCertificate.pdf
  - Computing skills for scientists: https://www.ccsf.edu/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerScience/ComputingSkillsforScientistsCertificate.pdf
  - JS specialist: http://www.ccsf.edu/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerNetworkingandInformationTechnology/JavaScriptSpecialistCertificate.pdf
  - Web site development techniques: http://www.ccsf.edu/content/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerNetworkingandInformationTechnology/WebSiteDevelopmentTechniquesCertificate.pdf 
  - Mobile web app development: http://www.ccsf.edu/content/dam/ccsf/documents/OfficeOfInstruction/Catalog/Programs/ComputerNetworkingandInformationTechnology/MobileWebAppDevelopmentCertificate.pdf


## Jobs
- Freelancing contracts:
  - https://www.docracy.com/0kpa5hfcobb/freelance-developer-contract
  - https://gist.github.com/malarkey/4031110
  - https://github.com/ashedryden/freelance-contract
  - https://gist.github.com/reubano/344656121394ef7ff2048ca8b006f7d2
- Freelancing tips/guides/tutorials:
  - https://gist.github.com/mdang/ef3669d4f266c62c3312
  - http://www.incomeinsiders.com/tag/freelance-programmer-contract/
- Remote/freelancing:
  - https://github.com/engineerapart/TheRemoteFreelancer
  - Indeed/indeed prime
  - Upwork/Fiverr
  - Weworkremotely programming jobs: https://weworkremotely.com/categories/remote-programming-jobs
- Repsonding to freelancing gig offers: http://jessicahische.is/helpingyouanswer  
- Codementor: https://www.codementor.io
- Juni: https://junilearning.com/
- General Assembly teaching: http://generalassemb.ly/how-we-work/teach-at-general-assembly
- Thinkful web dev instructor: https://jobs.chegg.com/search-results?category=Education
- Code for America: https://www.codeforamerica.org/jobs
- Slack internship: https://slack.com/careers/1852134/software-engineering-internship
- CCSF professor: https://jobs.ccsf.edu/
- SF student intern: http://www.sfstudentintern.org/


## Interview prep
- Interview questions: https://docs.google.com/document/d/1L2nqcMLxQeFHVd9ZOfgzZTjxWZsJLJe65rAzKfmldsM/edit
- Interview algorithms and tips: http://meetupresources.herokuapp.com/index.html
- Assorted interview tips: http://kelukelu.me/interview/questions.html
- Women Who Code Interview Prep: https://github.com/WomenWhoCode/Algorithms-InterviewPrep/wiki
- Gayle McDowell:
  - talk at Canadian University Software Engineering Conference: https://www.youtube.com/watch?v=rEJzOhC5ZtQ
  - Ask Me Anything video (see the top comment with all the links to the individual questions): https://www.youtube.com/watch?v=1fqxMuPmGak


## Stack Overflow
- Users I like:
  - https://stackoverflow.com/users/224132/
  - https://stackoverflow.com/users/895245/
  - https://stackoverflow.com/users/5459839/
  - https://stackoverflow.com/users/3000206/
  - https://stackoverflow.com/users/168657/
  - https://stackoverflow.com/users/559737/
  - https://stackoverflow.com/users/385378/
  - https://stackoverflow.com/users/1204143/
  - https://stackoverflow.com/users/128511/
  - https://stackoverflow.com/users/501557/
  - https://stackoverflow.com/users/1566221/


## Fun
- Regex to validate another regex: https://stackoverflow.com/questions/172303/is-there-a-regular-expression-to-detect-a-valid-regular-expression
- Quine: https://en.wikipedia.org/wiki/Quine_(computing)
- Hello World in every language: https://github.com/leachim6/hello-world
- 99 bottles of beer in 1500 different languages: http://www.99-bottles-of-beer.net/
- Tetris written in Conway's Game of Life: https://codegolf.stackexchange.com/questions/11880/build-a-working-game-of-tetris-in-conways-game-of-life
- FizzBuzz stuff: 
  - http://wiki.c2.com/?FizzBuzzTest
  - https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition
- Git man page generator: https://git-man-page-generator.lokaltog.net/

