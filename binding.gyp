{
    "targets": [
        {
            "target_name": "fasttext",
            "sources": [
                "vendor/fasttext/src/args.cc",
                "vendor/fasttext/src/args.h",
                "vendor/fasttext/src/dictionary.cc",
                "vendor/fasttext/src/dictionary.h",
                "vendor/fasttext/src/fasttext.cc",
                "vendor/fasttext/src/fasttext.h",
                "vendor/fasttext/src/matrix.cc",
                "vendor/fasttext/src/matrix.h",
                "vendor/fasttext/src/model.cc",
                "vendor/fasttext/src/model.h",
                "vendor/fasttext/src/productquantizer.cc",
                "vendor/fasttext/src/productquantizer.h",
                "vendor/fasttext/src/qmatrix.cc",
                "vendor/fasttext/src/qmatrix.h",
                "vendor/fasttext/src/real.h",
                "vendor/fasttext/src/utils.cc",
                "vendor/fasttext/src/utils.h",
                "vendor/fasttext/src/vector.cc",
                "vendor/fasttext/src/vector.h",
                "src/classifier.h",
                "src/classifierWorker.cc",
                "src/query.h",
                "src/nnWorker.cc",
                "src/wrapper.cc",
                "src/fasttext.cc"
            ],
            "include_dirs": ["<!(node -e \"require('nan')\")"],
            "cflags": [
                "-std=c++11",
                "-pthread",
                "-Wsign-compare",
                "-fexceptions",
                "-O0"
            ],
            "conditions": [
                [ 'OS!="win"', {
                    "cflags+": [ "-std=c++11", "-fexceptions" ],
                    "cflags_c+": [ "-std=c++11", "-fexceptions" ],
                    "cflags_cc+": [ "-std=c++11", "-fexceptions" ],
                }],
                [ 'OS=="mac"', {
                    "cflags+": [ "-stdlib=libc++" ],
                    "xcode_settings": {
                        "OTHER_CPLUSPLUSFLAGS" : [ "-std=c++11", "-stdlib=libc++", "-pthread" ],
                        "OTHER_LDFLAGS": [ "-stdlib=libc++" ],
                        "MACOSX_DEPLOYMENT_TARGET": "10.7",
                        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
                        "CLANG_CXX_LANGUAGE_STANDARD":"c++11",
                        "CLANG_CXX_LIBRARY": "libc++"
                    },
                }]
            ]
        },
        {
            "target_name": "action_after_build",
            "type": "none",
            "dependencies": [ "<(module_name)" ],
            "copies": [
                {
                    "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
                    "destination": "<(module_path)"
                }
            ]
        }
    ]
}