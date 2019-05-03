#pragma once

#include <rocksdb/db.h>
#include <rocksdb/status.h>
#include <rocksdb/options.h>
#include <rocksdb/iterator.h>
#include <rocksdb/slice.h>
#include <rocksdb/write_batch.h>
#include <rocksdb/table.h>
#include <rocksdb/filter_policy.h>
#include <rocksdb/cache.h>

using namespace rocksdb;

struct Blob {
  public:
    Status st;
    std::string data;
};

class py_DB {
  public:
    py_DB();
    Status Open(const Options& options, const std::string& name);
    Status Put(const WriteOptions& options, const std::string& key,
                     const std::string& value);
    Blob Get(const ReadOptions& options, const std::string& key);
    Status Write(const WriteOptions& options, WriteBatch& updates);
    Status Delete(const WriteOptions& options, const std::string& key);
    void Close();
    std::unique_ptr<Iterator> NewIterator(const ReadOptions& options);
    //FIXME: python gc
    ~py_DB();
  private:
    DB* db_ptr;
};