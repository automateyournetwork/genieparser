expected_output = {
    'module': {
        'Summary': {
            'allocated': 251089,
            'allocs': 363675,
            'frees': 363508,
            'requested': 248417,
        },
        'bcrdu_avl': {
            'allocated': 72,
            'allocs': 1,
            'frees': 0,
            'requested': 56,
        },
        'cdllib': {
            'allocated': 1688,
            'allocs': 390,
            'frees': 389,
            'requested': 1672,
        },
        'chunk': {
            'allocated': 3065,
            'allocs': 11,
            'frees': 4,
            'requested': 2953,
        },
        'dbal-batch-mgr': {
            'allocated': 5182,
            'allocs': 9,
            'frees': 6,
            'requested': 5134,
        },
        'dbal-bipc': {
            'allocated': 4657,
            'allocs': 26,
            'frees': 21,
            'requested': 4577,
        },
        'dbal-channel-mgr': {
            'allocated': 3264,
            'allocs': 12,
            'frees': 6,
            'requested': 3168,
        },
        'dbal-conn': {
            'allocated': 1024,
            'allocs': 61,
            'frees': 53,
            'requested': 896,
        },
        'dbal-exec-mgr': {
            'allocated': 0,
            'allocs': 59,
            'frees': 59,
            'requested': 0,
        },
        'dbal-intf-mgr': {
            'allocated': 439,
            'allocs': 12,
            'frees': 0,
            'requested': 247,
        },
        'dbal-mqipc': {
            'allocated': 0,
            'allocs': 8,
            'frees': 8,
            'requested': 0,
        },
        'dbal-root': {
            'allocated': 28,
            'allocs': 1,
            'frees': 0,
            'requested': 12,
        },
        'dbal-scn-mgr': {
            'allocated': 3160,
            'allocs': 4,
            'frees': 0,
            'requested': 3096,
        },
        'dbal-tunnel-mgr': {
            'allocated': 5279,
            'allocs': 55,
            'frees': 48,
            'requested': 5167,
        },
        'eiapi-hashtable': {
            'allocated': 104,
            'allocs': 6835,
            'frees': 6834,
            'requested': 88,
        },
        'eiapi-ht-array': {
            'allocated': 1552,
            'allocs': 6835,
            'frees': 6834,
            'requested': 1536,
        },
        'eiapi-iter': {
            'allocated': 0,
            'allocs': 3,
            'frees': 3,
            'requested': 0,
        },
        'eiapi-name': {
            'allocated': 0,
            'allocs': 2664,
            'frees': 2664,
            'requested': 0,
        },
        'eiapi-nlist': {
            'allocated': 0,
            'allocs': 677,
            'frees': 677,
            'requested': 0,
        },
        'eiapi-nlist-item': {
            'allocated': 0,
            'allocs': 1954,
            'frees': 1954,
            'requested': 0,
        },
        'eiapi-ntlist': {
            'allocated': 0,
            'allocs': 3,
            'frees': 3,
            'requested': 0,
        },
        'eiapi-ntlist-item': {
            'allocated': 0,
            'allocs': 117,
            'frees': 117,
            'requested': 0,
        },
        'eiapi-nvlist': {
            'allocated': 40,
            'allocs': 205,
            'frees': 204,
            'requested': 24,
        },
        'eiapi-nvlist-item': {
            'allocated': 80,
            'allocs': 1040,
            'frees': 1039,
            'requested': 64,
        },
        'eiapi-property': {
            'allocated': 0,
            'allocs': 593,
            'frees': 593,
            'requested': 0,
        },
        'eiapi-props': {
            'allocated': 0,
            'allocs': 7,
            'frees': 7,
            'requested': 0,
        },
        'eiapi-props-ht-elem': {
            'allocated': 0,
            'allocs': 36,
            'frees': 36,
            'requested': 0,
        },
        'eiapi-s-type-meta': {
            'allocated': 0,
            'allocs': 117,
            'frees': 117,
            'requested': 0,
        },
        'eiapi-strbuf': {
            'allocated': 0,
            'allocs': 2779,
            'frees': 2779,
            'requested': 0,
        },
        'eiapi-strbuf-misc': {
            'allocated': 0,
            'allocs': 2921,
            'frees': 2921,
            'requested': 0,
        },
        'eiapi-strdup': {
            'allocated': 30,
            'allocs': 90,
            'frees': 89,
            'requested': 14,
        },
        'eiapi-typedef-meta': {
            'allocated': 0,
            'allocs': 117,
            'frees': 117,
            'requested': 0,
        },
        'eiapi-uri': {
            'allocated': 880,
            'allocs': 41,
            'frees': 40,
            'requested': 864,
        },
        'eiapi-uri-sml-misc': {
            'allocated': 160,
            'allocs': 82,
            'frees': 80,
            'requested': 128,
        },
        'eiapi-util': {
            'allocated': 0,
            'allocs': 56,
            'frees': 56,
            'requested': 0,
        },
        'eiapi-value': {
            'allocated': 112,
            'allocs': 2094,
            'frees': 2092,
            'requested': 80,
        },
        'eiapi-value-misc': {
            'allocated': 0,
            'allocs': 63,
            'frees': 63,
            'requested': 0,
        },
        'eiapi-value-sml-misc': {
            'allocated': 48,
            'allocs': 1057,
            'frees': 1056,
            'requested': 32,
        },
        'eiapi-vlist': {
            'allocated': 40,
            'allocs': 700,
            'frees': 699,
            'requested': 24,
        },
        'eiapi-vlist-item': {
            'allocated': 40,
            'allocs': 2122,
            'frees': 2121,
            'requested': 24,
        },
        'eiapi-vtable': {
            'allocated': 0,
            'allocs': 3,
            'frees': 3,
            'requested': 0,
        },
        'eiapi-vtable-item': {
            'allocated': 0,
            'allocs': 3,
            'frees': 3,
            'requested': 0,
        },
        'error-wrong-component': {
            'allocated': 0,
            'allocs': 574,
            'frees': 574,
            'requested': 0,
        },
        'eventutil': {
            'allocated': 120685,
            'allocs': 784,
            'frees': 726,
            'requested': 119757,
        },
        'invalid': {
            'allocated': 22340,
            'allocs': 8,
            'frees': 0,
            'requested': 22212,
        },
        'libconfd': {
            'allocated': 552,
            'allocs': 60,
            'frees': 55,
            'requested': 472,
        },
        'ndbutil': {
            'allocated': 0,
            'allocs': 2,
            'frees': 2,
            'requested': 0,
        },
        'ndbutil-md-json': {
            'allocated': 0,
            'allocs': 108,
            'frees': 108,
            'requested': 0,
        },
        'ndbutil-md-loader-ht-e': {
            'allocated': 0,
            'allocs': 1647,
            'frees': 1647,
            'requested': 0,
        },
        'ndbutil-md-nsmeta': {
            'allocated': 0,
            'allocs': 108,
            'frees': 108,
            'requested': 0,
        },
        'ndbutil-md-schema-ht-e': {
            'allocated': 6789,
            'allocs': 706,
            'frees': 702,
            'requested': 6725,
        },
        'ndbutil-md-str': {
            'allocated': 0,
            'allocs': 317250,
            'frees': 317250,
            'requested': 0,
        },
        'ndbutil-md-str-struct': {
            'allocated': 5185,
            'allocs': 1570,
            'frees': 1566,
            'requested': 5121,
        },
        'ndbutil-md-util': {
            'allocated': 0,
            'allocs': 675,
            'frees': 675,
            'requested': 0,
        },
        'ndbutil-md-xfrm': {
            'allocated': 6779,
            'allocs': 85,
            'frees': 81,
            'requested': 6715,
        },
        'ndbutil-md-xfrm-choice': {
            'allocated': 11586,
            'allocs': 4,
            'frees': 0,
            'requested': 11522,
        },
        'ndbutil-metadata': {
            'allocated': 0,
            'allocs': 5103,
            'frees': 5103,
            'requested': 0,
        },
        'opssl-parser': {
            'allocated': 2102,
            'allocs': 2,
            'frees': 0,
            'requested': 2070,
        },
        'process': {
            'allocated': 16863,
            'allocs': 47,
            'frees': 42,
            'requested': 16783,
        },
        'uipeer': {
            'allocated': 27264,
            'allocs': 1079,
            'frees': 1074,
            'requested': 27184,
        },
    },
}
				