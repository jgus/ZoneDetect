#include "gtest/gtest.h"
#include "zonedetect.h"

TEST(ZoneDetect, ZDLookup) {
  std::unique_ptr<ZoneDetect, decltype(&ZDCloseDatabase)> db{
      ZDOpenDatabase(DB_PATH), &ZDCloseDatabase};
  ASSERT_NE(db, nullptr);

  std::unique_ptr<ZoneDetectResult, decltype(&ZDFreeResults)> results_denver{
      ZDLookup(db.get(), 39.7392, -104.9903, nullptr), &ZDFreeResults};
  ASSERT_NE(results_denver, nullptr);
  EXPECT_EQ(results_denver->lookupResult, ZD_LOOKUP_IN_ZONE);
}

TEST(ZoneDetect, ZDHelperSimpleLookupString) {
  std::unique_ptr<ZoneDetect, decltype(&ZDCloseDatabase)> db{
      ZDOpenDatabase(DB_PATH), &ZDCloseDatabase};
  ASSERT_NE(db, nullptr);

  std::unique_ptr<char, decltype(&ZDHelperSimpleLookupStringFree)> results_denver{
      ZDHelperSimpleLookupString(db.get(), 39.7392, -104.9903), &ZDHelperSimpleLookupStringFree};
  ASSERT_NE(results_denver, nullptr);
      std::string str_denver{results_denver.get()};
  EXPECT_EQ(str_denver, "America/Denver");
}
