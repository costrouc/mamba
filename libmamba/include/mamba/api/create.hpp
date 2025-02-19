// Copyright (c) 2019, QuantStack and Mamba Contributors
//
// Distributed under the terms of the BSD 3-Clause License.
//
// The full license is in the file LICENSE, distributed with this software.

#ifndef MAMBA_API_CREATE_HPP
#define MAMBA_API_CREATE_HPP


namespace mamba
{
    void create();

    namespace detail
    {
        void store_platform_config(const fs::path& prefix, const std::string& platform);
    }
}

#endif
