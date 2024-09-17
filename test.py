import sys
from os import path

import pytest
from definitions import PACKAGE_ROOT_PATH

if __name__ == "__main__":
    test_report_file_path = path.join(PACKAGE_ROOT_PATH, "reports/report.html")
    gen_report_cmd = "--html=%s" % test_report_file_path
    verbose_cmd = "-vv"
    gen_report_cmd_xml = "--junitxml=report.xml"

    sys.argv.append(gen_report_cmd)
    sys.argv.append(verbose_cmd)
    sys.argv.append(gen_report_cmd_xml)

    sys.exit(pytest.main(sys.argv[1:]))