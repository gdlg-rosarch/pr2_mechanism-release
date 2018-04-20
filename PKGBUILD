# Script generated with Bloom
pkgdesc="ROS - This package contains the C++ interfaces to the PR2 hardware components that are controlled over EtherCAT. This includes the motors and encoders needed to control the PR2 mechanism, as well as components like the pressure sensors in the fingertips, camera triggers, etc... All of the hardware components in this interface are directly available to the controllers inside the hard realtime control loop."
url='http://ros.org/wiki/pr2_hardware_interface'

pkgname='ros-kinetic-pr2-hardware-interface'
pkgver='1.8.17_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-roscpp'
)

depends=('ros-kinetic-geometry-msgs'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=pr2_hardware_interface
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_hardware_interface $srcdir/pr2_hardware_interface
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

