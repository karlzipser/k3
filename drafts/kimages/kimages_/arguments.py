from k3.utils3 import *

_project_name = fname(pname(pname(__file__)))


def get_args():
    
    import argparse

    par = argparse.ArgumentParser(
        prog=_project_name,
        description='display and rate from command line',
        fromfile_prefix_chars='@',
        add_help=True,
    ); aa = par.add_argument


    aa(
        '--files',
        '-f',
        nargs="+",
        default=[],
        help='space-separated list of image files to show',
    )
    aa(
        '--paths',
        '-p',
        nargs="+",
        default=[],
        help='space-separated list of paths',
    )
    aa(
        '--ignore_paths',
        '-ip',
        nargs="+",
        default=[],
        help='space-separated list of paths to ignore',
    )


    aa(
        '--change',
        '-c',
        nargs='?',
        const=True,
        default=False,
        help="allow change",
    )    
    aa(
        '--random',
        '-r',
        nargs='?',
        const=True,
        default=False,
        help="randomize display order",
    )
    aa(
        '--progressive_range',
        '-pr',
        nargs='?',
        const=True,
        default=False,
        help='view with progressive rating range',
    )
    aa(
        "--hist",
        nargs='?',
        const=True, default=False,
        help="make histogram of ratings"
    )
    aa(
        "--cmd_lines",
        nargs='?',
        const=True,
        default=False,
        help="print command lines used so far"
    )
    aa(
        "--view_once",
        "-vo",
        nargs='?',
        const=True,
        default=False,
        help="don't view image if already rated",
    )
    aa(
        "--slideshow",
        "-s",
        nargs='?',
        const=True,
        default=False,
        help="slideshow mode",
    )
    aa(
        "--descend",
        "-d",
        nargs='?',
        const=True,
        default=False,
        help="descend directories collecting images"
    )

    aa(
        '--screen_pro',
        '-sp',
        action='store',
        type=float,
        required=False,
        default=0.9, 
        help='proportion of screen to use',
    )
    aa(
        '--topic',
        '-tp',
        action='store',
        type=str,
        required=True,
        default='no_name', 
        help='name of topic of images',
    )
    aa(
        '--project_name',
        action='store',
        type=str,
        required=False,
        default=_project_name, #fnamene(__file__), 
        help='name project, used in saving log data',
    )


    aa(
        '--add_as',
        action='store',
        type=float,
        required=False,
        default=0, 
        help='add images as rating given ',
    )
    aa(
        '--min_rating',
        '-mn',
        action='store',
        type=float,
        required=False,
        default=0, 
        help='minmum rating (1-9) to display',
    )
    aa(
        '--max_rating',
        '-mx',
        action='store',
        type=float,
        required=False,
        default=10, 
        help='maximum rating (1-9) to display',
    )
    aa(
        '--mwidth',
        action='store',
        type=int,
        required=False,
        default=400, 
        help='min width',
    )
    aa(
        '--window_x',
        action='store',
        type=int,
        required=False,
        default=-1, 
        help='window x upper left corner',
    )
    aa(
        '--window_y',
        action='store',
        type=int,
        required=False,
        default=-1, 
        help='window y upper left corner',
    )
    aa(
        '--view_n',
        action='store',
        type=int,
        required=False,
        default=0, 
        help='rate up to n views',
    )
    aa(
        '--mheight',
        action='store',
        type=int,
        required=False,
        default=400, 
        help='min height',
    )
    aa(
        '--seconds',
        '-sc',
        action='store',
        type=float,
        required=False,
        default=1.0, 
        help='slideshow display seconds',
    )

    args = par.parse_args()

    assert not(args.view_once and args.view_n)

    return args

#EOF
