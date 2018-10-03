#include <gtest/gtest.h>
#include "attribute_parser.h"

using namespace std;

GTEST_TEST(ParserTest, tag) {
    string line = "<tag1 value = \"HelloWorld\">";
    EXPECT_EQ("tag1", parse_tag_name(line));
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}