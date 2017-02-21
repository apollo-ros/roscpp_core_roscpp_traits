Name:           ros-lunar-roscpp-serialization
Version:        0.6.2
Release:        0%{?dist}
Summary:        ROS roscpp_serialization package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roscpp_serialization
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-cpp-common
Requires:       ros-lunar-roscpp-traits
Requires:       ros-lunar-rostime
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cpp-common
BuildRequires:  ros-lunar-roscpp-traits
BuildRequires:  ros-lunar-rostime

%description
roscpp_serialization contains the code for serialization as described in
MessagesSerializationAndAdaptingTypes. This package is a component of roscpp.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Feb 21 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.6.2-0
- Autogenerated by Bloom

