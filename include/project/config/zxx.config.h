#ifndef _CONFIG_H_

#define _CONFIG_H_

#ifndef ZXX_PUBLIC
#ifndef ZXX_INTERNAL

    #ifdef _WIN32
        #if defined(BUILD_SHARED)
            #define ZXX_PUBLIC __declspec(dllexport)
            #define ZXX_INTERNAL
        #elif defined(BUILD_STATIC)
            #define ZXX_PUBLIC __declspec(dllimport)
            #define ZXX_INTERNAL
        #else
            #define ZXX_PUBLIC
            #define ZXX_INTERNAL
        #endif 

    #else
        #define ZXX_PUBLIC __attribute__((visibility("default")))
        #define ZXX_INTERNAL __attribute__((visibility("hidden")))

#endif // WIN32 || _WIN32

#endif // !ZXX_INTERNAL
#endif // !ZXX_PUBLIC

#if __cplusplus > 201703L
    // C++20 and later
    #define DARRAY_HAS_CONSTEXPR 1
    #define DARRAY_HAS_NODISCARD 1
    #define DARRAY_HAS_INLINE_VARIABLES 1
#elif __cplusplus > 201402L
    // C++17
    #define DARRAY_HAS_CONSTEXPR 1
    #define DARRAY_HAS_NODISCARD 1
#elif __cplusplus > 201103L
// C++11
    #define HAS_CONSTEXPR 1
#else
// C++98/03
#endif

#ifdef HAS_CONSTEXPR
    #define ZXX_CONSTEXPR constexpr
#else
    #define ZXX_CONSTEXPR
#endif

#ifdef HAS_NODISCARD
    #define ZXX_NODISCARD [[nodiscard]]
#else
    #define ZXX_NODISCARD
#endif

#ifdef CAN_FORCE_INLINE
    #define ZXX_FORCE_INLINE inline
#else
    #define ZXX_FORCE_INLINE
#endif


#if __cplusplus >= 201703L

    #define BEGIN_NS_ZXX_CORE_CONTAINER namespace zxx::core::container {
    #define END_NS_ZXX_CORE_CONTAINER }

#else

    #define BEGIN_NS_ZXX_CORE_CONTAINER             \
        namespace zxx {                             \
                namespace core {                    \
                    namespace container {           

    #define END_NS_ZXX_CORE_CONTAINER  }}}
#endif

#if __cplusplus >= 201703L

    #define BEGIN_NS_ZXX_CORE_CONTAINER_TEST namespace zxx::core::container::test {
    #define END_NS_ZXX_CORE_CONTAINER_TEST }

#else

    #define BEGIN_NS_ZXX_CORE_CONTAINER_TEST        \
        namespace zxx {                             \
                namespace core {                    \
                    namespace container {           \
                        namespace test {            

    #define END_NS_ZXX_CORE_CONTAINER_TEST  }}}}
#endif


#endif // !_ZXX_CONFIG_H